from Database.db_connection import db_connection_func
from Libraries.logs import print_action_logs as pal
from psycopg2 import OperationalError, DatabaseError

def get_urls():
    try:
        connection_string = db_connection_func()
    except:
        print("MAL")
    else:

        try:
            select = connection_string.cursor()

            global login_url
            select.execute("SELECT CONCAT(url_base, url_path) FROM test.web_pages WHERE id = 1")
            login_url = select.fetchone()[0]

            global login_url_name
            select.execute("SELECT name FROM test.web_pages WHERE id = 1")
            login_url_name = select.fetchone()[0]

            global home_url
            select.execute("SELECT CONCAT(url_base, url_path) FROM test.web_pages WHERE id = 2")
            home_url = select.fetchone()[0]

            global home_url_name
            select.execute("SELECT name FROM test.web_pages WHERE id = 2")
            home_url_name = select.fetchone()[0]

        except:
            print("Ha ocurrido un error durante la ejecución de las consultas")
        finally:
            select.close()
    finally:
        connection_string.close()

get_urls()