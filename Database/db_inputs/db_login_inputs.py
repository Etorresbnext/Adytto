from Database.db_connection import db_connection_func
from Libraries.logs import print_action_logs as pal
from psycopg2 import OperationalError, DatabaseError


def db_login_inputs():
    try:
        connection_string = db_connection_func()
        dbname = connection_string.info.dbname
        global script_progress, script_success, total_active_users_log
    except OperationalError as oe:
        print(f"{oe}")
    else:

        try:
            # Cursor para realizar consultas a Base de Datos
            select = connection_string.cursor()

            script_progress = pal(f"Realizando consultas a la Base de Datos: {dbname}")

            global total_active_users
            select.execute("SELECT COUNT(*) FROM test.users WHERE active = true")
            total_active_users = select.fetchone()[0]

            global user_information
            select.execute("SELECT * FROM test.get_users_configuration()")
            user_information = select.fetchall()

        except DatabaseError as de:
            print(f"{de}")
        else:
            script_success = pal("Consultas realizadas con éxito. Extrayendo información de usuarios...")
            total_active_users_log = pal(f"Total de Usuarios Activos y No Borrados: {total_active_users}")
        finally:
            select.close()
    finally:
        connection_string.close()

db_login_inputs()