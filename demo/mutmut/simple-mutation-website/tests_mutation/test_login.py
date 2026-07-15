import unittest
import pytest
from datastore.users import create_user, check_login
from datastore.store import Store # Import Store
from data.config import Config
from datastore.connection import Connection
import os

class TestLogin(unittest.TestCase):
    def setUp(self):
        # 1. Use a clean test database file
        self.db_path = 'test_login.db'
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
            
        self.config = Config(
            database_filename=self.db_path,
            data_directory='.',
            migrations_filename='data/migrations.json', # Ensure this path is correct
            password_secret='secret'
        )
        
        # 2. RUN MIGRATIONS: This creates the tables automatically
        Store.migrate_db(self.config)

    def tearDown(self):
        # Cleanup
        if os.path.exists(self.db_path):
            os.remove(self.db_path)