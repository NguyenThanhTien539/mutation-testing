import os.path
import json
from sqlite3 import Error
from datastore.connection import Connection


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁStoreǁmigrate_db__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStoreǁcheck_schema_version__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStoreǁexecute_migration__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStoreǁimport_test_data__mutmut: MutantDict = {}  # type: ignore


class Store:

    @staticmethod
    @_mutmut_mutated(mutants_xǁStoreǁmigrate_db__mutmut)
    def migrate_db(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_orig(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_1(conf):
        schema_version = None

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_2(conf):
        schema_version = Store.check_schema_version(None)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_3(conf):
        schema_version = Store.check_schema_version(conf)

        file = None
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_4(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(None, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_5(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, None)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_6(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_7(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, )
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_8(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = ""
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_9(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(None, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_10(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, None) as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_11(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open('r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_12(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, ) as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_13(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'XXrXX') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_14(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'R') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_15(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = None
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_16(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(None)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_17(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["XXmigrationsXX"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_18(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["MIGRATIONS"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_19(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["XXversionXX"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_20(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["VERSION"] > schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_21(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] >= schema_version:
                    Store.execute_migration(m, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_22(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(None, conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_23(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, None)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_24(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(conf)

    @staticmethod
    def xǁStoreǁmigrate_db__mutmut_25(conf):
        schema_version = Store.check_schema_version(conf)

        file = os.path.join(conf.data_directory, conf.migrations_filename)
        data = None
        with open(file, 'r') as f:
            data = json.load(f)
        if data:
            for m in data["migrations"]:
                if m["version"] > schema_version:
                    Store.execute_migration(m, )

    @staticmethod
    @_mutmut_mutated(mutants_xǁStoreǁcheck_schema_version__mutmut)
    def check_schema_version(conf):
        schema_version = 0
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'select max(version) from migrations;'
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = row[0]
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_orig(conf):
        schema_version = 0
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'select max(version) from migrations;'
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = row[0]
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_1(conf):
        schema_version = None
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'select max(version) from migrations;'
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = row[0]
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_2(conf):
        schema_version = 1
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'select max(version) from migrations;'
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = row[0]
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_3(conf):
        schema_version = 0
        with Connection(None) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'select max(version) from migrations;'
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = row[0]
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_4(conf):
        schema_version = 0
        with Connection(conf) as db_connection:
            try:
                c = None
                sql = 'select max(version) from migrations;'
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = row[0]
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_5(conf):
        schema_version = 0
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = None
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = row[0]
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_6(conf):
        schema_version = 0
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'XXselect max(version) from migrations;XX'
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = row[0]
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_7(conf):
        schema_version = 0
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'SELECT MAX(VERSION) FROM MIGRATIONS;'
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = row[0]
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_8(conf):
        schema_version = 0
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'select max(version) from migrations;'
                row = None
                if row:
                    schema_version = row[0]
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_9(conf):
        schema_version = 0
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'select max(version) from migrations;'
                row = c.execute(None).fetchone()
                if row:
                    schema_version = row[0]
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_10(conf):
        schema_version = 0
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'select max(version) from migrations;'
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = None
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_11(conf):
        schema_version = 0
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'select max(version) from migrations;'
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = row[1]
            except Error as err:
                print(err)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_12(conf):
        schema_version = 0
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'select max(version) from migrations;'
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = row[0]
            except Error as err:
                print(None)
        print(f'max schema version = {schema_version}')
        return schema_version

    @staticmethod
    def xǁStoreǁcheck_schema_version__mutmut_13(conf):
        schema_version = 0
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = 'select max(version) from migrations;'
                row = c.execute(sql).fetchone()
                if row:
                    schema_version = row[0]
            except Error as err:
                print(err)
        print(None)
        return schema_version

    @staticmethod
    @_mutmut_mutated(mutants_xǁStoreǁexecute_migration__mutmut)
    def execute_migration(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_orig(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_1(migration, conf):
        with Connection(None) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_2(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = None
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_3(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = None
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_4(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["XXsqlXX"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_5(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["SQL"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_6(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(None)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_7(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(None)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_8(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = None
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_9(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["XXversionXX"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_10(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["VERSION"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_11(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["XXcommentXX"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_12(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["COMMENT"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_13(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(None)
                c.execute(sql)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_14(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(None)
            except Error as err:
                print(err)

    @staticmethod
    def xǁStoreǁexecute_migration__mutmut_15(migration, conf):
        with Connection(conf) as db_connection:
            try:
                c = db_connection.cursor()
                sql = migration["sql"]
                print(sql)
                c.execute(sql)
                sql = f'insert into migrations values (\'{migration["version"]}\', \'{migration["comment"]}\', CURRENT_TIMESTAMP);'
                print(sql)
                c.execute(sql)
            except Error as err:
                print(None)

    @staticmethod
    @_mutmut_mutated(mutants_xǁStoreǁimport_test_data__mutmut)
    def import_test_data(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_orig(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_1(conf, table, json_data_file):
        print(None)
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_2(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = ""
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_3(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(None, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_4(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, None) as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_5(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open('r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_6(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, ) as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_7(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'XXrXX') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_8(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'R') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_9(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = None
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_10(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(None)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_11(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(None) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_12(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = None
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_13(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = None
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_14(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(None)
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_15(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = None
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_16(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(None)
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_17(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = None
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_18(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[2:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_19(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:+1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_20(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-2]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_21(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = None
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_22(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace(None, "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_23(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", None)
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_24(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_25(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", )
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_26(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[2:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_27(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:+1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_28(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-2].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_29(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("XX'CURRENT_TIMESTAMP'XX", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_30(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'current_timestamp'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_31(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "XXCURRENT_TIMESTAMPXX")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_32(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "current_timestamp")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_33(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = None
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_34(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(None)
                        c.execute(sql)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_35(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(None)
                except Error as err:
                    print(err)

    @staticmethod
    def xǁStoreǁimport_test_data__mutmut_36(conf, table, json_data_file):
        print(f'importing data to {table} from {json_data_file}')
        data = None
        with open(json_data_file, 'r') as f:
            data = json.load(f)
        if data:
            with Connection(conf) as db_connection:
                try:
                    c = db_connection.cursor()
                    for item in data:
                        columns = list(item.keys())
                        values = []
                        for k in columns:
                            values.append(item[k])
                        cols = f'{columns}'[1:-1]
                        vals = f'{values}'[1:-1].replace("'CURRENT_TIMESTAMP'", "CURRENT_TIMESTAMP")
                        sql = f'insert into {table}({cols}) values ({vals});'
                        print(sql)
                        c.execute(sql)
                except Error as err:
                    print(None)

mutants_xǁStoreǁmigrate_db__mutmut['_mutmut_orig'] = Store.xǁStoreǁmigrate_db__mutmut_orig # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_1'] = Store.xǁStoreǁmigrate_db__mutmut_1 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_2'] = Store.xǁStoreǁmigrate_db__mutmut_2 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_3'] = Store.xǁStoreǁmigrate_db__mutmut_3 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_4'] = Store.xǁStoreǁmigrate_db__mutmut_4 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_5'] = Store.xǁStoreǁmigrate_db__mutmut_5 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_6'] = Store.xǁStoreǁmigrate_db__mutmut_6 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_7'] = Store.xǁStoreǁmigrate_db__mutmut_7 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_8'] = Store.xǁStoreǁmigrate_db__mutmut_8 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_9'] = Store.xǁStoreǁmigrate_db__mutmut_9 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_10'] = Store.xǁStoreǁmigrate_db__mutmut_10 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_11'] = Store.xǁStoreǁmigrate_db__mutmut_11 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_12'] = Store.xǁStoreǁmigrate_db__mutmut_12 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_13'] = Store.xǁStoreǁmigrate_db__mutmut_13 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_14'] = Store.xǁStoreǁmigrate_db__mutmut_14 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_15'] = Store.xǁStoreǁmigrate_db__mutmut_15 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_16'] = Store.xǁStoreǁmigrate_db__mutmut_16 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_17'] = Store.xǁStoreǁmigrate_db__mutmut_17 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_18'] = Store.xǁStoreǁmigrate_db__mutmut_18 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_19'] = Store.xǁStoreǁmigrate_db__mutmut_19 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_20'] = Store.xǁStoreǁmigrate_db__mutmut_20 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_21'] = Store.xǁStoreǁmigrate_db__mutmut_21 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_22'] = Store.xǁStoreǁmigrate_db__mutmut_22 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_23'] = Store.xǁStoreǁmigrate_db__mutmut_23 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_24'] = Store.xǁStoreǁmigrate_db__mutmut_24 # type: ignore # mutmut generated
mutants_xǁStoreǁmigrate_db__mutmut['xǁStoreǁmigrate_db__mutmut_25'] = Store.xǁStoreǁmigrate_db__mutmut_25 # type: ignore # mutmut generated

mutants_xǁStoreǁcheck_schema_version__mutmut['_mutmut_orig'] = Store.xǁStoreǁcheck_schema_version__mutmut_orig # type: ignore # mutmut generated
mutants_xǁStoreǁcheck_schema_version__mutmut['xǁStoreǁcheck_schema_version__mutmut_1'] = Store.xǁStoreǁcheck_schema_version__mutmut_1 # type: ignore # mutmut generated
mutants_xǁStoreǁcheck_schema_version__mutmut['xǁStoreǁcheck_schema_version__mutmut_2'] = Store.xǁStoreǁcheck_schema_version__mutmut_2 # type: ignore # mutmut generated
mutants_xǁStoreǁcheck_schema_version__mutmut['xǁStoreǁcheck_schema_version__mutmut_3'] = Store.xǁStoreǁcheck_schema_version__mutmut_3 # type: ignore # mutmut generated
mutants_xǁStoreǁcheck_schema_version__mutmut['xǁStoreǁcheck_schema_version__mutmut_4'] = Store.xǁStoreǁcheck_schema_version__mutmut_4 # type: ignore # mutmut generated
mutants_xǁStoreǁcheck_schema_version__mutmut['xǁStoreǁcheck_schema_version__mutmut_5'] = Store.xǁStoreǁcheck_schema_version__mutmut_5 # type: ignore # mutmut generated
mutants_xǁStoreǁcheck_schema_version__mutmut['xǁStoreǁcheck_schema_version__mutmut_6'] = Store.xǁStoreǁcheck_schema_version__mutmut_6 # type: ignore # mutmut generated
mutants_xǁStoreǁcheck_schema_version__mutmut['xǁStoreǁcheck_schema_version__mutmut_7'] = Store.xǁStoreǁcheck_schema_version__mutmut_7 # type: ignore # mutmut generated
mutants_xǁStoreǁcheck_schema_version__mutmut['xǁStoreǁcheck_schema_version__mutmut_8'] = Store.xǁStoreǁcheck_schema_version__mutmut_8 # type: ignore # mutmut generated
mutants_xǁStoreǁcheck_schema_version__mutmut['xǁStoreǁcheck_schema_version__mutmut_9'] = Store.xǁStoreǁcheck_schema_version__mutmut_9 # type: ignore # mutmut generated
mutants_xǁStoreǁcheck_schema_version__mutmut['xǁStoreǁcheck_schema_version__mutmut_10'] = Store.xǁStoreǁcheck_schema_version__mutmut_10 # type: ignore # mutmut generated
mutants_xǁStoreǁcheck_schema_version__mutmut['xǁStoreǁcheck_schema_version__mutmut_11'] = Store.xǁStoreǁcheck_schema_version__mutmut_11 # type: ignore # mutmut generated
mutants_xǁStoreǁcheck_schema_version__mutmut['xǁStoreǁcheck_schema_version__mutmut_12'] = Store.xǁStoreǁcheck_schema_version__mutmut_12 # type: ignore # mutmut generated
mutants_xǁStoreǁcheck_schema_version__mutmut['xǁStoreǁcheck_schema_version__mutmut_13'] = Store.xǁStoreǁcheck_schema_version__mutmut_13 # type: ignore # mutmut generated

mutants_xǁStoreǁexecute_migration__mutmut['_mutmut_orig'] = Store.xǁStoreǁexecute_migration__mutmut_orig # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_1'] = Store.xǁStoreǁexecute_migration__mutmut_1 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_2'] = Store.xǁStoreǁexecute_migration__mutmut_2 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_3'] = Store.xǁStoreǁexecute_migration__mutmut_3 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_4'] = Store.xǁStoreǁexecute_migration__mutmut_4 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_5'] = Store.xǁStoreǁexecute_migration__mutmut_5 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_6'] = Store.xǁStoreǁexecute_migration__mutmut_6 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_7'] = Store.xǁStoreǁexecute_migration__mutmut_7 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_8'] = Store.xǁStoreǁexecute_migration__mutmut_8 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_9'] = Store.xǁStoreǁexecute_migration__mutmut_9 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_10'] = Store.xǁStoreǁexecute_migration__mutmut_10 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_11'] = Store.xǁStoreǁexecute_migration__mutmut_11 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_12'] = Store.xǁStoreǁexecute_migration__mutmut_12 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_13'] = Store.xǁStoreǁexecute_migration__mutmut_13 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_14'] = Store.xǁStoreǁexecute_migration__mutmut_14 # type: ignore # mutmut generated
mutants_xǁStoreǁexecute_migration__mutmut['xǁStoreǁexecute_migration__mutmut_15'] = Store.xǁStoreǁexecute_migration__mutmut_15 # type: ignore # mutmut generated

mutants_xǁStoreǁimport_test_data__mutmut['_mutmut_orig'] = Store.xǁStoreǁimport_test_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_1'] = Store.xǁStoreǁimport_test_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_2'] = Store.xǁStoreǁimport_test_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_3'] = Store.xǁStoreǁimport_test_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_4'] = Store.xǁStoreǁimport_test_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_5'] = Store.xǁStoreǁimport_test_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_6'] = Store.xǁStoreǁimport_test_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_7'] = Store.xǁStoreǁimport_test_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_8'] = Store.xǁStoreǁimport_test_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_9'] = Store.xǁStoreǁimport_test_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_10'] = Store.xǁStoreǁimport_test_data__mutmut_10 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_11'] = Store.xǁStoreǁimport_test_data__mutmut_11 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_12'] = Store.xǁStoreǁimport_test_data__mutmut_12 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_13'] = Store.xǁStoreǁimport_test_data__mutmut_13 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_14'] = Store.xǁStoreǁimport_test_data__mutmut_14 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_15'] = Store.xǁStoreǁimport_test_data__mutmut_15 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_16'] = Store.xǁStoreǁimport_test_data__mutmut_16 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_17'] = Store.xǁStoreǁimport_test_data__mutmut_17 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_18'] = Store.xǁStoreǁimport_test_data__mutmut_18 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_19'] = Store.xǁStoreǁimport_test_data__mutmut_19 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_20'] = Store.xǁStoreǁimport_test_data__mutmut_20 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_21'] = Store.xǁStoreǁimport_test_data__mutmut_21 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_22'] = Store.xǁStoreǁimport_test_data__mutmut_22 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_23'] = Store.xǁStoreǁimport_test_data__mutmut_23 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_24'] = Store.xǁStoreǁimport_test_data__mutmut_24 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_25'] = Store.xǁStoreǁimport_test_data__mutmut_25 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_26'] = Store.xǁStoreǁimport_test_data__mutmut_26 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_27'] = Store.xǁStoreǁimport_test_data__mutmut_27 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_28'] = Store.xǁStoreǁimport_test_data__mutmut_28 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_29'] = Store.xǁStoreǁimport_test_data__mutmut_29 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_30'] = Store.xǁStoreǁimport_test_data__mutmut_30 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_31'] = Store.xǁStoreǁimport_test_data__mutmut_31 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_32'] = Store.xǁStoreǁimport_test_data__mutmut_32 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_33'] = Store.xǁStoreǁimport_test_data__mutmut_33 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_34'] = Store.xǁStoreǁimport_test_data__mutmut_34 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_35'] = Store.xǁStoreǁimport_test_data__mutmut_35 # type: ignore # mutmut generated
mutants_xǁStoreǁimport_test_data__mutmut['xǁStoreǁimport_test_data__mutmut_36'] = Store.xǁStoreǁimport_test_data__mutmut_36 # type: ignore # mutmut generated

