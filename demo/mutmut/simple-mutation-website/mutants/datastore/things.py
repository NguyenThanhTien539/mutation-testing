

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_all_things__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_get_all_things__mutmut)
def get_all_things(db):
    rows = db.execute('SELECT * from things').fetchall()
    things = []
    if rows and len(rows) > 0:
        for row in rows:
            things.append(dict(row))
    return things
def x_get_all_things__mutmut_orig(db):
    rows = db.execute('SELECT * from things').fetchall()
    things = []
    if rows and len(rows) > 0:
        for row in rows:
            things.append(dict(row))
    return things
def x_get_all_things__mutmut_1(db):
    rows = None
    things = []
    if rows and len(rows) > 0:
        for row in rows:
            things.append(dict(row))
    return things
def x_get_all_things__mutmut_2(db):
    rows = db.execute(None).fetchall()
    things = []
    if rows and len(rows) > 0:
        for row in rows:
            things.append(dict(row))
    return things
def x_get_all_things__mutmut_3(db):
    rows = db.execute('XXSELECT * from thingsXX').fetchall()
    things = []
    if rows and len(rows) > 0:
        for row in rows:
            things.append(dict(row))
    return things
def x_get_all_things__mutmut_4(db):
    rows = db.execute('select * from things').fetchall()
    things = []
    if rows and len(rows) > 0:
        for row in rows:
            things.append(dict(row))
    return things
def x_get_all_things__mutmut_5(db):
    rows = db.execute('SELECT * FROM THINGS').fetchall()
    things = []
    if rows and len(rows) > 0:
        for row in rows:
            things.append(dict(row))
    return things
def x_get_all_things__mutmut_6(db):
    rows = db.execute('SELECT * from things').fetchall()
    things = None
    if rows and len(rows) > 0:
        for row in rows:
            things.append(dict(row))
    return things
def x_get_all_things__mutmut_7(db):
    rows = db.execute('SELECT * from things').fetchall()
    things = []
    if rows or len(rows) > 0:
        for row in rows:
            things.append(dict(row))
    return things
def x_get_all_things__mutmut_8(db):
    rows = db.execute('SELECT * from things').fetchall()
    things = []
    if rows and len(rows) >= 0:
        for row in rows:
            things.append(dict(row))
    return things
def x_get_all_things__mutmut_9(db):
    rows = db.execute('SELECT * from things').fetchall()
    things = []
    if rows and len(rows) > 1:
        for row in rows:
            things.append(dict(row))
    return things
def x_get_all_things__mutmut_10(db):
    rows = db.execute('SELECT * from things').fetchall()
    things = []
    if rows and len(rows) > 0:
        for row in rows:
            things.append(None)
    return things
def x_get_all_things__mutmut_11(db):
    rows = db.execute('SELECT * from things').fetchall()
    things = []
    if rows and len(rows) > 0:
        for row in rows:
            things.append(dict(None))
    return things

mutants_x_get_all_things__mutmut['_mutmut_orig'] = x_get_all_things__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_all_things__mutmut['x_get_all_things__mutmut_1'] = x_get_all_things__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_all_things__mutmut['x_get_all_things__mutmut_2'] = x_get_all_things__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_all_things__mutmut['x_get_all_things__mutmut_3'] = x_get_all_things__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_all_things__mutmut['x_get_all_things__mutmut_4'] = x_get_all_things__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_all_things__mutmut['x_get_all_things__mutmut_5'] = x_get_all_things__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_all_things__mutmut['x_get_all_things__mutmut_6'] = x_get_all_things__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_all_things__mutmut['x_get_all_things__mutmut_7'] = x_get_all_things__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_all_things__mutmut['x_get_all_things__mutmut_8'] = x_get_all_things__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_all_things__mutmut['x_get_all_things__mutmut_9'] = x_get_all_things__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_all_things__mutmut['x_get_all_things__mutmut_10'] = x_get_all_things__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_all_things__mutmut['x_get_all_things__mutmut_11'] = x_get_all_things__mutmut_11 # type: ignore # mutmut generated
