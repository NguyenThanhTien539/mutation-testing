import hashlib


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_calculate_password_hash__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_calculate_password_hash__mutmut)
def calculate_password_hash(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(string, encoding='utf-8'))
    password_hash = module.hexdigest()
    return password_hash


def x_calculate_password_hash__mutmut_orig(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(string, encoding='utf-8'))
    password_hash = module.hexdigest()
    return password_hash


def x_calculate_password_hash__mutmut_1(config, password):
    secret = None
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(string, encoding='utf-8'))
    password_hash = module.hexdigest()
    return password_hash


def x_calculate_password_hash__mutmut_2(config, password):
    secret = config.password_secret
    module = None
    string = f'{password}+{secret}'
    module.update(bytes(string, encoding='utf-8'))
    password_hash = module.hexdigest()
    return password_hash


def x_calculate_password_hash__mutmut_3(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = None
    module.update(bytes(string, encoding='utf-8'))
    password_hash = module.hexdigest()
    return password_hash


def x_calculate_password_hash__mutmut_4(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(None)
    password_hash = module.hexdigest()
    return password_hash


def x_calculate_password_hash__mutmut_5(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(None, encoding='utf-8'))
    password_hash = module.hexdigest()
    return password_hash


def x_calculate_password_hash__mutmut_6(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(string, encoding=None))
    password_hash = module.hexdigest()
    return password_hash


def x_calculate_password_hash__mutmut_7(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(encoding='utf-8'))
    password_hash = module.hexdigest()
    return password_hash


def x_calculate_password_hash__mutmut_8(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(string, ))
    password_hash = module.hexdigest()
    return password_hash


def x_calculate_password_hash__mutmut_9(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(string, encoding='XXutf-8XX'))
    password_hash = module.hexdigest()
    return password_hash


def x_calculate_password_hash__mutmut_10(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(string, encoding='UTF-8'))
    password_hash = module.hexdigest()
    return password_hash


def x_calculate_password_hash__mutmut_11(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(string, encoding='utf-8'))
    password_hash = None
    return password_hash

mutants_x_calculate_password_hash__mutmut['_mutmut_orig'] = x_calculate_password_hash__mutmut_orig # type: ignore # mutmut generated
mutants_x_calculate_password_hash__mutmut['x_calculate_password_hash__mutmut_1'] = x_calculate_password_hash__mutmut_1 # type: ignore # mutmut generated
mutants_x_calculate_password_hash__mutmut['x_calculate_password_hash__mutmut_2'] = x_calculate_password_hash__mutmut_2 # type: ignore # mutmut generated
mutants_x_calculate_password_hash__mutmut['x_calculate_password_hash__mutmut_3'] = x_calculate_password_hash__mutmut_3 # type: ignore # mutmut generated
mutants_x_calculate_password_hash__mutmut['x_calculate_password_hash__mutmut_4'] = x_calculate_password_hash__mutmut_4 # type: ignore # mutmut generated
mutants_x_calculate_password_hash__mutmut['x_calculate_password_hash__mutmut_5'] = x_calculate_password_hash__mutmut_5 # type: ignore # mutmut generated
mutants_x_calculate_password_hash__mutmut['x_calculate_password_hash__mutmut_6'] = x_calculate_password_hash__mutmut_6 # type: ignore # mutmut generated
mutants_x_calculate_password_hash__mutmut['x_calculate_password_hash__mutmut_7'] = x_calculate_password_hash__mutmut_7 # type: ignore # mutmut generated
mutants_x_calculate_password_hash__mutmut['x_calculate_password_hash__mutmut_8'] = x_calculate_password_hash__mutmut_8 # type: ignore # mutmut generated
mutants_x_calculate_password_hash__mutmut['x_calculate_password_hash__mutmut_9'] = x_calculate_password_hash__mutmut_9 # type: ignore # mutmut generated
mutants_x_calculate_password_hash__mutmut['x_calculate_password_hash__mutmut_10'] = x_calculate_password_hash__mutmut_10 # type: ignore # mutmut generated
mutants_x_calculate_password_hash__mutmut['x_calculate_password_hash__mutmut_11'] = x_calculate_password_hash__mutmut_11 # type: ignore # mutmut generated
mutants_x_create_user__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_user__mutmut)
def create_user(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_orig(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_1(db, config, firstname, lastname, username, password):
    password_hash = None
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_2(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(None, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_3(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, None)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_4(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_5(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, )
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_6(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = None
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_7(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        None,
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_8(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        None)
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_9(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_10(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        )
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_11(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'XXINSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);XX',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_12(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'insert into users(firstname, lastname, created_at, is_admin) values(?, ?, current_timestamp, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_13(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO USERS(FIRSTNAME, LASTNAME, CREATED_AT, IS_ADMIN) VALUES(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_14(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = None
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_15(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = None

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_16(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 >= 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_17(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 1:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_18(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = None

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_19(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            None,
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_20(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            None).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_21(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_22(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            ).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_23(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "XXINSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');XX",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_24(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "insert into auth_methods(user_id, username, password, type) values(?, ?, ?, 'username_and_password');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_25(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO AUTH_METHODS(USER_ID, USERNAME, PASSWORD, TYPE) VALUES(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def x_create_user__mutmut_26(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 >= 0:
            return True

    return False


def x_create_user__mutmut_27(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 1:
            return True

    return False


def x_create_user__mutmut_28(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return False

    return False


def x_create_user__mutmut_29(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return True

mutants_x_create_user__mutmut['_mutmut_orig'] = x_create_user__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_1'] = x_create_user__mutmut_1 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_2'] = x_create_user__mutmut_2 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_3'] = x_create_user__mutmut_3 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_4'] = x_create_user__mutmut_4 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_5'] = x_create_user__mutmut_5 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_6'] = x_create_user__mutmut_6 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_7'] = x_create_user__mutmut_7 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_8'] = x_create_user__mutmut_8 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_9'] = x_create_user__mutmut_9 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_10'] = x_create_user__mutmut_10 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_11'] = x_create_user__mutmut_11 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_12'] = x_create_user__mutmut_12 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_13'] = x_create_user__mutmut_13 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_14'] = x_create_user__mutmut_14 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_15'] = x_create_user__mutmut_15 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_16'] = x_create_user__mutmut_16 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_17'] = x_create_user__mutmut_17 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_18'] = x_create_user__mutmut_18 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_19'] = x_create_user__mutmut_19 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_20'] = x_create_user__mutmut_20 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_21'] = x_create_user__mutmut_21 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_22'] = x_create_user__mutmut_22 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_23'] = x_create_user__mutmut_23 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_24'] = x_create_user__mutmut_24 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_25'] = x_create_user__mutmut_25 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_26'] = x_create_user__mutmut_26 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_27'] = x_create_user__mutmut_27 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_28'] = x_create_user__mutmut_28 # type: ignore # mutmut generated
mutants_x_create_user__mutmut['x_create_user__mutmut_29'] = x_create_user__mutmut_29 # type: ignore # mutmut generated
mutants_x_check_login__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_check_login__mutmut)
def check_login(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_orig(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_1(db, config, username, password):
    password_hash = None
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_2(db, config, username, password):
    password_hash = calculate_password_hash(None, password)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_3(db, config, username, password):
    password_hash = calculate_password_hash(config, None)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_4(db, config, username, password):
    password_hash = calculate_password_hash(password)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_5(db, config, username, password):
    password_hash = calculate_password_hash(config, )
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_6(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = None
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_7(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        None,
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_8(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        None).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_9(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_10(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        ).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_11(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'XXSELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'XX',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_12(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'select user_id from auth_methods where username=? and password=? and type=\'username_and_password\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_13(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'SELECT USER_ID FROM AUTH_METHODS WHERE USERNAME=? AND PASSWORD=? AND TYPE=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def x_check_login__mutmut_14(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(None)
    return -1


def x_check_login__mutmut_15(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['XXuser_idXX'])
    return -1


def x_check_login__mutmut_16(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['USER_ID'])
    return -1


def x_check_login__mutmut_17(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return +1


def x_check_login__mutmut_18(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -2

mutants_x_check_login__mutmut['_mutmut_orig'] = x_check_login__mutmut_orig # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_1'] = x_check_login__mutmut_1 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_2'] = x_check_login__mutmut_2 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_3'] = x_check_login__mutmut_3 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_4'] = x_check_login__mutmut_4 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_5'] = x_check_login__mutmut_5 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_6'] = x_check_login__mutmut_6 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_7'] = x_check_login__mutmut_7 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_8'] = x_check_login__mutmut_8 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_9'] = x_check_login__mutmut_9 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_10'] = x_check_login__mutmut_10 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_11'] = x_check_login__mutmut_11 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_12'] = x_check_login__mutmut_12 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_13'] = x_check_login__mutmut_13 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_14'] = x_check_login__mutmut_14 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_15'] = x_check_login__mutmut_15 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_16'] = x_check_login__mutmut_16 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_17'] = x_check_login__mutmut_17 # type: ignore # mutmut generated
mutants_x_check_login__mutmut['x_check_login__mutmut_18'] = x_check_login__mutmut_18 # type: ignore # mutmut generated
mutants_x_check_admin__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_check_admin__mutmut)
def check_admin(db, username):
    user = user_by_username(db, username)
    if user:
        return bool(user["is_admin"])
    else:
        return False


def x_check_admin__mutmut_orig(db, username):
    user = user_by_username(db, username)
    if user:
        return bool(user["is_admin"])
    else:
        return False


def x_check_admin__mutmut_1(db, username):
    user = None
    if user:
        return bool(user["is_admin"])
    else:
        return False


def x_check_admin__mutmut_2(db, username):
    user = user_by_username(None, username)
    if user:
        return bool(user["is_admin"])
    else:
        return False


def x_check_admin__mutmut_3(db, username):
    user = user_by_username(db, None)
    if user:
        return bool(user["is_admin"])
    else:
        return False


def x_check_admin__mutmut_4(db, username):
    user = user_by_username(username)
    if user:
        return bool(user["is_admin"])
    else:
        return False


def x_check_admin__mutmut_5(db, username):
    user = user_by_username(db, )
    if user:
        return bool(user["is_admin"])
    else:
        return False


def x_check_admin__mutmut_6(db, username):
    user = user_by_username(db, username)
    if user:
        return bool(None)
    else:
        return False


def x_check_admin__mutmut_7(db, username):
    user = user_by_username(db, username)
    if user:
        return bool(user["XXis_adminXX"])
    else:
        return False


def x_check_admin__mutmut_8(db, username):
    user = user_by_username(db, username)
    if user:
        return bool(user["IS_ADMIN"])
    else:
        return False


def x_check_admin__mutmut_9(db, username):
    user = user_by_username(db, username)
    if user:
        return bool(user["is_admin"])
    else:
        return True

mutants_x_check_admin__mutmut['_mutmut_orig'] = x_check_admin__mutmut_orig # type: ignore # mutmut generated
mutants_x_check_admin__mutmut['x_check_admin__mutmut_1'] = x_check_admin__mutmut_1 # type: ignore # mutmut generated
mutants_x_check_admin__mutmut['x_check_admin__mutmut_2'] = x_check_admin__mutmut_2 # type: ignore # mutmut generated
mutants_x_check_admin__mutmut['x_check_admin__mutmut_3'] = x_check_admin__mutmut_3 # type: ignore # mutmut generated
mutants_x_check_admin__mutmut['x_check_admin__mutmut_4'] = x_check_admin__mutmut_4 # type: ignore # mutmut generated
mutants_x_check_admin__mutmut['x_check_admin__mutmut_5'] = x_check_admin__mutmut_5 # type: ignore # mutmut generated
mutants_x_check_admin__mutmut['x_check_admin__mutmut_6'] = x_check_admin__mutmut_6 # type: ignore # mutmut generated
mutants_x_check_admin__mutmut['x_check_admin__mutmut_7'] = x_check_admin__mutmut_7 # type: ignore # mutmut generated
mutants_x_check_admin__mutmut['x_check_admin__mutmut_8'] = x_check_admin__mutmut_8 # type: ignore # mutmut generated
mutants_x_check_admin__mutmut['x_check_admin__mutmut_9'] = x_check_admin__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_user_by_id__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_user_by_id__mutmut)
def get_user_by_id(db, user_id):
    row = db.execute('SELECT * from users where id=?', (user_id,)).fetchone()
    if row:
        user = dict(row)
        return user
    return None


def x_get_user_by_id__mutmut_orig(db, user_id):
    row = db.execute('SELECT * from users where id=?', (user_id,)).fetchone()
    if row:
        user = dict(row)
        return user
    return None


def x_get_user_by_id__mutmut_1(db, user_id):
    row = None
    if row:
        user = dict(row)
        return user
    return None


def x_get_user_by_id__mutmut_2(db, user_id):
    row = db.execute(None, (user_id,)).fetchone()
    if row:
        user = dict(row)
        return user
    return None


def x_get_user_by_id__mutmut_3(db, user_id):
    row = db.execute('SELECT * from users where id=?', None).fetchone()
    if row:
        user = dict(row)
        return user
    return None


def x_get_user_by_id__mutmut_4(db, user_id):
    row = db.execute((user_id,)).fetchone()
    if row:
        user = dict(row)
        return user
    return None


def x_get_user_by_id__mutmut_5(db, user_id):
    row = db.execute('SELECT * from users where id=?', ).fetchone()
    if row:
        user = dict(row)
        return user
    return None


def x_get_user_by_id__mutmut_6(db, user_id):
    row = db.execute('XXSELECT * from users where id=?XX', (user_id,)).fetchone()
    if row:
        user = dict(row)
        return user
    return None


def x_get_user_by_id__mutmut_7(db, user_id):
    row = db.execute('select * from users where id=?', (user_id,)).fetchone()
    if row:
        user = dict(row)
        return user
    return None


def x_get_user_by_id__mutmut_8(db, user_id):
    row = db.execute('SELECT * FROM USERS WHERE ID=?', (user_id,)).fetchone()
    if row:
        user = dict(row)
        return user
    return None


def x_get_user_by_id__mutmut_9(db, user_id):
    row = db.execute('SELECT * from users where id=?', (user_id,)).fetchone()
    if row:
        user = None
        return user
    return None


def x_get_user_by_id__mutmut_10(db, user_id):
    row = db.execute('SELECT * from users where id=?', (user_id,)).fetchone()
    if row:
        user = dict(None)
        return user
    return None

mutants_x_get_user_by_id__mutmut['_mutmut_orig'] = x_get_user_by_id__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_user_by_id__mutmut['x_get_user_by_id__mutmut_1'] = x_get_user_by_id__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_user_by_id__mutmut['x_get_user_by_id__mutmut_2'] = x_get_user_by_id__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_user_by_id__mutmut['x_get_user_by_id__mutmut_3'] = x_get_user_by_id__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_user_by_id__mutmut['x_get_user_by_id__mutmut_4'] = x_get_user_by_id__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_user_by_id__mutmut['x_get_user_by_id__mutmut_5'] = x_get_user_by_id__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_user_by_id__mutmut['x_get_user_by_id__mutmut_6'] = x_get_user_by_id__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_user_by_id__mutmut['x_get_user_by_id__mutmut_7'] = x_get_user_by_id__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_user_by_id__mutmut['x_get_user_by_id__mutmut_8'] = x_get_user_by_id__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_user_by_id__mutmut['x_get_user_by_id__mutmut_9'] = x_get_user_by_id__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_user_by_id__mutmut['x_get_user_by_id__mutmut_10'] = x_get_user_by_id__mutmut_10 # type: ignore # mutmut generated
mutants_x_user_by_username__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_user_by_username__mutmut)
def user_by_username(db, username):
    user_id = user_id_by_username(db, username)
    return get_user_by_id(db, user_id)


def x_user_by_username__mutmut_orig(db, username):
    user_id = user_id_by_username(db, username)
    return get_user_by_id(db, user_id)


def x_user_by_username__mutmut_1(db, username):
    user_id = None
    return get_user_by_id(db, user_id)


def x_user_by_username__mutmut_2(db, username):
    user_id = user_id_by_username(None, username)
    return get_user_by_id(db, user_id)


def x_user_by_username__mutmut_3(db, username):
    user_id = user_id_by_username(db, None)
    return get_user_by_id(db, user_id)


def x_user_by_username__mutmut_4(db, username):
    user_id = user_id_by_username(username)
    return get_user_by_id(db, user_id)


def x_user_by_username__mutmut_5(db, username):
    user_id = user_id_by_username(db, )
    return get_user_by_id(db, user_id)


def x_user_by_username__mutmut_6(db, username):
    user_id = user_id_by_username(db, username)
    return get_user_by_id(None, user_id)


def x_user_by_username__mutmut_7(db, username):
    user_id = user_id_by_username(db, username)
    return get_user_by_id(db, None)


def x_user_by_username__mutmut_8(db, username):
    user_id = user_id_by_username(db, username)
    return get_user_by_id(user_id)


def x_user_by_username__mutmut_9(db, username):
    user_id = user_id_by_username(db, username)
    return get_user_by_id(db, )

mutants_x_user_by_username__mutmut['_mutmut_orig'] = x_user_by_username__mutmut_orig # type: ignore # mutmut generated
mutants_x_user_by_username__mutmut['x_user_by_username__mutmut_1'] = x_user_by_username__mutmut_1 # type: ignore # mutmut generated
mutants_x_user_by_username__mutmut['x_user_by_username__mutmut_2'] = x_user_by_username__mutmut_2 # type: ignore # mutmut generated
mutants_x_user_by_username__mutmut['x_user_by_username__mutmut_3'] = x_user_by_username__mutmut_3 # type: ignore # mutmut generated
mutants_x_user_by_username__mutmut['x_user_by_username__mutmut_4'] = x_user_by_username__mutmut_4 # type: ignore # mutmut generated
mutants_x_user_by_username__mutmut['x_user_by_username__mutmut_5'] = x_user_by_username__mutmut_5 # type: ignore # mutmut generated
mutants_x_user_by_username__mutmut['x_user_by_username__mutmut_6'] = x_user_by_username__mutmut_6 # type: ignore # mutmut generated
mutants_x_user_by_username__mutmut['x_user_by_username__mutmut_7'] = x_user_by_username__mutmut_7 # type: ignore # mutmut generated
mutants_x_user_by_username__mutmut['x_user_by_username__mutmut_8'] = x_user_by_username__mutmut_8 # type: ignore # mutmut generated
mutants_x_user_by_username__mutmut['x_user_by_username__mutmut_9'] = x_user_by_username__mutmut_9 # type: ignore # mutmut generated
mutants_x_user_id_by_username__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_user_id_by_username__mutmut)
def user_id_by_username(db, username):
    row = db.execute("SELECT user_id from auth_methods where username=? and type='USERNAME_AND_PASSWORD'", (username,)).fetchone()
    if row:
        user_id = int(row["user_id"])
        return user_id
    return None


def x_user_id_by_username__mutmut_orig(db, username):
    row = db.execute("SELECT user_id from auth_methods where username=? and type='USERNAME_AND_PASSWORD'", (username,)).fetchone()
    if row:
        user_id = int(row["user_id"])
        return user_id
    return None


def x_user_id_by_username__mutmut_1(db, username):
    row = None
    if row:
        user_id = int(row["user_id"])
        return user_id
    return None


def x_user_id_by_username__mutmut_2(db, username):
    row = db.execute(None, (username,)).fetchone()
    if row:
        user_id = int(row["user_id"])
        return user_id
    return None


def x_user_id_by_username__mutmut_3(db, username):
    row = db.execute("SELECT user_id from auth_methods where username=? and type='USERNAME_AND_PASSWORD'", None).fetchone()
    if row:
        user_id = int(row["user_id"])
        return user_id
    return None


def x_user_id_by_username__mutmut_4(db, username):
    row = db.execute((username,)).fetchone()
    if row:
        user_id = int(row["user_id"])
        return user_id
    return None


def x_user_id_by_username__mutmut_5(db, username):
    row = db.execute("SELECT user_id from auth_methods where username=? and type='USERNAME_AND_PASSWORD'", ).fetchone()
    if row:
        user_id = int(row["user_id"])
        return user_id
    return None


def x_user_id_by_username__mutmut_6(db, username):
    row = db.execute("XXSELECT user_id from auth_methods where username=? and type='USERNAME_AND_PASSWORD'XX", (username,)).fetchone()
    if row:
        user_id = int(row["user_id"])
        return user_id
    return None


def x_user_id_by_username__mutmut_7(db, username):
    row = db.execute("select user_id from auth_methods where username=? and type='username_and_password'", (username,)).fetchone()
    if row:
        user_id = int(row["user_id"])
        return user_id
    return None


def x_user_id_by_username__mutmut_8(db, username):
    row = db.execute("SELECT USER_ID FROM AUTH_METHODS WHERE USERNAME=? AND TYPE='USERNAME_AND_PASSWORD'", (username,)).fetchone()
    if row:
        user_id = int(row["user_id"])
        return user_id
    return None


def x_user_id_by_username__mutmut_9(db, username):
    row = db.execute("SELECT user_id from auth_methods where username=? and type='USERNAME_AND_PASSWORD'", (username,)).fetchone()
    if row:
        user_id = None
        return user_id
    return None


def x_user_id_by_username__mutmut_10(db, username):
    row = db.execute("SELECT user_id from auth_methods where username=? and type='USERNAME_AND_PASSWORD'", (username,)).fetchone()
    if row:
        user_id = int(None)
        return user_id
    return None


def x_user_id_by_username__mutmut_11(db, username):
    row = db.execute("SELECT user_id from auth_methods where username=? and type='USERNAME_AND_PASSWORD'", (username,)).fetchone()
    if row:
        user_id = int(row["XXuser_idXX"])
        return user_id
    return None


def x_user_id_by_username__mutmut_12(db, username):
    row = db.execute("SELECT user_id from auth_methods where username=? and type='USERNAME_AND_PASSWORD'", (username,)).fetchone()
    if row:
        user_id = int(row["USER_ID"])
        return user_id
    return None

mutants_x_user_id_by_username__mutmut['_mutmut_orig'] = x_user_id_by_username__mutmut_orig # type: ignore # mutmut generated
mutants_x_user_id_by_username__mutmut['x_user_id_by_username__mutmut_1'] = x_user_id_by_username__mutmut_1 # type: ignore # mutmut generated
mutants_x_user_id_by_username__mutmut['x_user_id_by_username__mutmut_2'] = x_user_id_by_username__mutmut_2 # type: ignore # mutmut generated
mutants_x_user_id_by_username__mutmut['x_user_id_by_username__mutmut_3'] = x_user_id_by_username__mutmut_3 # type: ignore # mutmut generated
mutants_x_user_id_by_username__mutmut['x_user_id_by_username__mutmut_4'] = x_user_id_by_username__mutmut_4 # type: ignore # mutmut generated
mutants_x_user_id_by_username__mutmut['x_user_id_by_username__mutmut_5'] = x_user_id_by_username__mutmut_5 # type: ignore # mutmut generated
mutants_x_user_id_by_username__mutmut['x_user_id_by_username__mutmut_6'] = x_user_id_by_username__mutmut_6 # type: ignore # mutmut generated
mutants_x_user_id_by_username__mutmut['x_user_id_by_username__mutmut_7'] = x_user_id_by_username__mutmut_7 # type: ignore # mutmut generated
mutants_x_user_id_by_username__mutmut['x_user_id_by_username__mutmut_8'] = x_user_id_by_username__mutmut_8 # type: ignore # mutmut generated
mutants_x_user_id_by_username__mutmut['x_user_id_by_username__mutmut_9'] = x_user_id_by_username__mutmut_9 # type: ignore # mutmut generated
mutants_x_user_id_by_username__mutmut['x_user_id_by_username__mutmut_10'] = x_user_id_by_username__mutmut_10 # type: ignore # mutmut generated
mutants_x_user_id_by_username__mutmut['x_user_id_by_username__mutmut_11'] = x_user_id_by_username__mutmut_11 # type: ignore # mutmut generated
mutants_x_user_id_by_username__mutmut['x_user_id_by_username__mutmut_12'] = x_user_id_by_username__mutmut_12 # type: ignore # mutmut generated
