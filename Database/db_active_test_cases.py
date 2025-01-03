from Database.db_connection import db_connection_func
from Libraries.logs import print_action_logs as pal
from psycopg2 import OperationalError, DatabaseError

def active_test_cases():
    try:
        connection_string = db_connection_func()
    except:
        print("ERROR")
    else:

        try:
            select = connection_string.cursor()

            global test_case_one
            select.execute("SELECT active FROM test.test_cases WHERE id = 1")
            test_case_one = select.fetchone()[0]

            global test_case_two
            select.execute("SELECT active FROM test.test_cases WHERE id = 2")
            test_case_two = select.fetchone()[0]

        except:
            print("Error en consulta")
        finally:
            select.close()
    finally:
        connection_string.close()

active_test_cases()

tco = test_case_one
tct = test_case_two