from Database.db_connection import db_connection_func
from Libraries.logs import print_action_logs as pal
from psycopg2 import OperationalError, DatabaseError

def home_web_objects():
    try:
        connection_string = db_connection_func()
    except:
        print("Error")
    else:

        try:
            # Cursor para realizar consultas a Base de Datos
            select = connection_string.cursor()

            # Obtener los agrupadores para el objeto btn_initials
            global btn_initials_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 13")
            btn_initials_object_name = select.fetchone()[0]

            global btn_initials_grouper_id
            select.execute("SELECT id_grouper FROM test.web_objects WHERE id = 13")
            btn_initials_grouper_id = select.fetchone()[0]

            global btn_initials_grouper_class
            select.execute("SELECT class_grouper FROM test.web_objects WHERE id = 13")
            btn_initials_grouper_class = select.fetchone()[0]

            global btn_initials_grouper_xpath
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 13")
            btn_initials_grouper_xpath = select.fetchone()[0]


            # Obtener los agrupadores para el objeto card_initials
            global card_initials_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 14")
            card_initials_object_name = select.fetchone()[0]

            global card_initials_grouper_class
            select.execute("SELECT class_grouper FROM test.web_objects WHERE id = 14")
            card_initials_grouper_class = select.fetchone()[0]

            global card_initials_grouper_xpath
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 14")
            card_initials_grouper_xpath = select.fetchone()[0]


            # Obtener los agrupadores para el objeto card_initials
            global btn_logout_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 15")
            btn_logout_object_name = select.fetchone()[0]

            global btn_logout_grouper_class
            select.execute("SELECT class_grouper FROM test.web_objects WHERE id = 15")
            btn_logout_grouper_class = select.fetchone()[0]

            global btn_logout_grouper_xpath
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 15")
            btn_logout_grouper_xpath = select.fetchone()[0]

        except:
            print("Error en consulta")
        finally:
            select.close()
    finally:
        connection_string.close()

home_web_objects()