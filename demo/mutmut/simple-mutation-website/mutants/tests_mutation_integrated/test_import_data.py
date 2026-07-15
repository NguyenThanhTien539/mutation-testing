# tests_mutation/test_import_data.py

import unittest
import os
import pytest
from datastore.store import Store
from data.config import Config
from datastore.connection import Connection

class TestImportData(unittest.TestCase):
    def setUp(self):
        # 1. Ensure we use a clean test database
        self.db_path = 'test_import.db'
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
            
        # 2. Configure specifically for this test
        self.config = Config(
            database_filename=self.db_path,
            data_directory='.', # Assuming migrations.json is in the root
            migrations_filename='data/migrations.json'
        )
        
        # 3. CRITICAL: Initialize the database schema
        # This will create 'users', 'auth_methods', and 'things'
        Store.migrate_db(self.config)
        
        # Path to your JSON data
        self.test_json = 'tests_mutation_integrated/things.json' 

    def test_import_things(self):
        # Now that migrations have run, the 'things' table exists
        Store.import_test_data(self.config, 'things', self.test_json)
        
        with Connection(self.config) as db:
            rows = db.execute('SELECT count(*) FROM things').fetchone()
            self.assertEqual(rows[0], 3, "Should have imported exactly 3 items")