from Database.db_connection import db_connection_func
from Libraries.logs import print_action_logs as pal
from psycopg2 import OperationalError, DatabaseError

def get_browsers_for_test_execution():
    try:
        connection_string = db_connection_func()
    except OperationalError as oe:
        print(f"{oe}")
    else:

        select = connection_string.cursor()

        global login_execution
        select.execute("SELECT * FROM  test.get_browsers_for_test_execution(1)")
        login_execution = select.fetchone()

        global logout_execution
        select.execute("SELECT * FROM  test.get_browsers_for_test_execution(2)")
        logout_execution = select.fetchone()

        global config_execution
        select.execute("SELECT * FROM  test.get_browsers_for_test_execution(3)")
        config_execution = select.fetchone()

        global config_pages_load
        select.execute("SELECT * FROM  test.get_browsers_for_test_execution(4)")
        config_pages_load = select.fetchone()

        select.close()
    finally:
        connection_string.close()

get_browsers_for_test_execution()