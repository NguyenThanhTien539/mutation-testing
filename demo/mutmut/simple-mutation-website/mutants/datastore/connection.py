import sqlite3
from sqlite3 import Error
import os


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁConnectionǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁConnectionǁ__enter____mutmut: MutantDict = {}  # type: ignore
mutants_xǁConnectionǁ__exit____mutmut: MutantDict = {}  # type: ignore
mutants_xǁConnectionǁcreate_connection__mutmut: MutantDict = {}  # type: ignore


class Connection(object):
    @_mutmut_mutated(mutants_xǁConnectionǁ__init____mutmut)
    def __init__(self, conf):
        self.config = conf
        self.database_filename = os.path.join(conf.data_directory, conf.db_filename)
        self.db_connection = None
    def xǁConnectionǁ__init____mutmut_orig(self, conf):
        self.config = conf
        self.database_filename = os.path.join(conf.data_directory, conf.db_filename)
        self.db_connection = None
    def xǁConnectionǁ__init____mutmut_1(self, conf):
        self.config = None
        self.database_filename = os.path.join(conf.data_directory, conf.db_filename)
        self.db_connection = None
    def xǁConnectionǁ__init____mutmut_2(self, conf):
        self.config = conf
        self.database_filename = None
        self.db_connection = None
    def xǁConnectionǁ__init____mutmut_3(self, conf):
        self.config = conf
        self.database_filename = os.path.join(None, conf.db_filename)
        self.db_connection = None
    def xǁConnectionǁ__init____mutmut_4(self, conf):
        self.config = conf
        self.database_filename = os.path.join(conf.data_directory, None)
        self.db_connection = None
    def xǁConnectionǁ__init____mutmut_5(self, conf):
        self.config = conf
        self.database_filename = os.path.join(conf.db_filename)
        self.db_connection = None
    def xǁConnectionǁ__init____mutmut_6(self, conf):
        self.config = conf
        self.database_filename = os.path.join(conf.data_directory, )
        self.db_connection = None
    def xǁConnectionǁ__init____mutmut_7(self, conf):
        self.config = conf
        self.database_filename = os.path.join(conf.data_directory, conf.db_filename)
        self.db_connection = ""

    @_mutmut_mutated(mutants_xǁConnectionǁ__enter____mutmut)
    def __enter__(self):
        self.db_connection = self.create_connection()
        return self.db_connection

    def xǁConnectionǁ__enter____mutmut_orig(self):
        self.db_connection = self.create_connection()
        return self.db_connection

    def xǁConnectionǁ__enter____mutmut_1(self):
        self.db_connection = None
        return self.db_connection

    @_mutmut_mutated(mutants_xǁConnectionǁ__exit____mutmut)
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value or exc_type or traceback:
            print(exc_value)
            print(exc_type)
            print(traceback)
        self.db_connection.commit()
        self.db_connection.close()

    def xǁConnectionǁ__exit____mutmut_orig(self, exc_type, exc_value, traceback):
        if exc_value or exc_type or traceback:
            print(exc_value)
            print(exc_type)
            print(traceback)
        self.db_connection.commit()
        self.db_connection.close()

    def xǁConnectionǁ__exit____mutmut_1(self, exc_type, exc_value, traceback):
        if exc_value or exc_type and traceback:
            print(exc_value)
            print(exc_type)
            print(traceback)
        self.db_connection.commit()
        self.db_connection.close()

    def xǁConnectionǁ__exit____mutmut_2(self, exc_type, exc_value, traceback):
        if exc_value and exc_type or traceback:
            print(exc_value)
            print(exc_type)
            print(traceback)
        self.db_connection.commit()
        self.db_connection.close()

    def xǁConnectionǁ__exit____mutmut_3(self, exc_type, exc_value, traceback):
        if exc_value or exc_type or traceback:
            print(None)
            print(exc_type)
            print(traceback)
        self.db_connection.commit()
        self.db_connection.close()

    def xǁConnectionǁ__exit____mutmut_4(self, exc_type, exc_value, traceback):
        if exc_value or exc_type or traceback:
            print(exc_value)
            print(None)
            print(traceback)
        self.db_connection.commit()
        self.db_connection.close()

    def xǁConnectionǁ__exit____mutmut_5(self, exc_type, exc_value, traceback):
        if exc_value or exc_type or traceback:
            print(exc_value)
            print(exc_type)
            print(None)
        self.db_connection.commit()
        self.db_connection.close()

    @_mutmut_mutated(mutants_xǁConnectionǁcreate_connection__mutmut)
    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.database_filename)
            return conn
        except Error as e:
            print(e)
        return conn

    def xǁConnectionǁcreate_connection__mutmut_orig(self):
        conn = None
        try:
            conn = sqlite3.connect(self.database_filename)
            return conn
        except Error as e:
            print(e)
        return conn

    def xǁConnectionǁcreate_connection__mutmut_1(self):
        conn = ""
        try:
            conn = sqlite3.connect(self.database_filename)
            return conn
        except Error as e:
            print(e)
        return conn

    def xǁConnectionǁcreate_connection__mutmut_2(self):
        conn = None
        try:
            conn = None
            return conn
        except Error as e:
            print(e)
        return conn

    def xǁConnectionǁcreate_connection__mutmut_3(self):
        conn = None
        try:
            conn = sqlite3.connect(None)
            return conn
        except Error as e:
            print(e)
        return conn

    def xǁConnectionǁcreate_connection__mutmut_4(self):
        conn = None
        try:
            conn = sqlite3.connect(self.database_filename)
            return conn
        except Error as e:
            print(None)
        return conn

mutants_xǁConnectionǁ__init____mutmut['_mutmut_orig'] = Connection.xǁConnectionǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁConnectionǁ__init____mutmut['xǁConnectionǁ__init____mutmut_1'] = Connection.xǁConnectionǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁConnectionǁ__init____mutmut['xǁConnectionǁ__init____mutmut_2'] = Connection.xǁConnectionǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁConnectionǁ__init____mutmut['xǁConnectionǁ__init____mutmut_3'] = Connection.xǁConnectionǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁConnectionǁ__init____mutmut['xǁConnectionǁ__init____mutmut_4'] = Connection.xǁConnectionǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁConnectionǁ__init____mutmut['xǁConnectionǁ__init____mutmut_5'] = Connection.xǁConnectionǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁConnectionǁ__init____mutmut['xǁConnectionǁ__init____mutmut_6'] = Connection.xǁConnectionǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁConnectionǁ__init____mutmut['xǁConnectionǁ__init____mutmut_7'] = Connection.xǁConnectionǁ__init____mutmut_7 # type: ignore # mutmut generated

mutants_xǁConnectionǁ__enter____mutmut['_mutmut_orig'] = Connection.xǁConnectionǁ__enter____mutmut_orig # type: ignore # mutmut generated
mutants_xǁConnectionǁ__enter____mutmut['xǁConnectionǁ__enter____mutmut_1'] = Connection.xǁConnectionǁ__enter____mutmut_1 # type: ignore # mutmut generated

mutants_xǁConnectionǁ__exit____mutmut['_mutmut_orig'] = Connection.xǁConnectionǁ__exit____mutmut_orig # type: ignore # mutmut generated
mutants_xǁConnectionǁ__exit____mutmut['xǁConnectionǁ__exit____mutmut_1'] = Connection.xǁConnectionǁ__exit____mutmut_1 # type: ignore # mutmut generated
mutants_xǁConnectionǁ__exit____mutmut['xǁConnectionǁ__exit____mutmut_2'] = Connection.xǁConnectionǁ__exit____mutmut_2 # type: ignore # mutmut generated
mutants_xǁConnectionǁ__exit____mutmut['xǁConnectionǁ__exit____mutmut_3'] = Connection.xǁConnectionǁ__exit____mutmut_3 # type: ignore # mutmut generated
mutants_xǁConnectionǁ__exit____mutmut['xǁConnectionǁ__exit____mutmut_4'] = Connection.xǁConnectionǁ__exit____mutmut_4 # type: ignore # mutmut generated
mutants_xǁConnectionǁ__exit____mutmut['xǁConnectionǁ__exit____mutmut_5'] = Connection.xǁConnectionǁ__exit____mutmut_5 # type: ignore # mutmut generated

mutants_xǁConnectionǁcreate_connection__mutmut['_mutmut_orig'] = Connection.xǁConnectionǁcreate_connection__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConnectionǁcreate_connection__mutmut['xǁConnectionǁcreate_connection__mutmut_1'] = Connection.xǁConnectionǁcreate_connection__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConnectionǁcreate_connection__mutmut['xǁConnectionǁcreate_connection__mutmut_2'] = Connection.xǁConnectionǁcreate_connection__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConnectionǁcreate_connection__mutmut['xǁConnectionǁcreate_connection__mutmut_3'] = Connection.xǁConnectionǁcreate_connection__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConnectionǁcreate_connection__mutmut['xǁConnectionǁcreate_connection__mutmut_4'] = Connection.xǁConnectionǁcreate_connection__mutmut_4 # type: ignore # mutmut generated
