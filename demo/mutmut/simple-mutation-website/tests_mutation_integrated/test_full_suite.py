import unittest
import sqlite3
import pytest
import os
from data.config import Config
from datastore.store import Store
from datastore.connection import Connection
from datastore.users import create_user, check_login, check_admin, get_user_by_id
from datastore.things import get_all_things

class TestFullSuite(unittest.TestCase):
    def setUp(self):
        self.db_path = 'full_test.db'
        self.config = Config(
            database_filename=self.db_path,
            data_directory='.',
            migrations_filename='data/migrations.json',
            password_secret='my-secret'
        )
        Store.migrate_db(self.config)
        
        # FIX: Ensure the connection returns rows as dictionaries
        with Connection(self.config) as db:
            db.row_factory = sqlite3.Row

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    # Testing users.py
    def test_user_lifecycle(self):
        with Connection(self.config) as db:
            # FIX: Apply row_factory to this specific connection
            db.row_factory = sqlite3.Row
            
            # Create
            success = create_user(db, self.config, "John", "Doe", "jdoe", "password123")
            self.assertTrue(success)
            
            # Login
            user_id = check_login(db, self.config, "jdoe", "password123")
            self.assertNotEqual(user_id, -1)
            
            # Admin check
            self.assertFalse(check_admin(db, "jdoe"))
            
            # Retrieve
            user = get_user_by_id(db, user_id)
            self.assertEqual(user['firstname'], "John")

    # Testing things.py
    def test_get_all_things(self):
        with Connection(self.config) as db:
            # FIX: Apply row_factory to this specific connection
            db.row_factory = sqlite3.Row
            
            # Manually insert to test retrieval
            db.execute("INSERT INTO things (name) VALUES ('item1')")
            db.commit()
            
            things = get_all_things(db)
            self.assertEqual(len(things), 1)
            self.assertEqual(things[0]['name'], 'item1')