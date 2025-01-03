from Database.db_connection import db_connection_func
from Libraries.logs import print_action_logs as pal
from psycopg2 import OperationalError, DatabaseError

def start_inputs():
    try:
        connection_string = db_connection_func()
        dbname = connection_string.info.dbname
        global connection_success, script_progress, script_success, script_select_user, script_select_test_set
    except OperationalError as oe:
        print(f"No ha sido posible conectarse a la Base de Datos {dbname}: {oe}")
    else:
        connection_success = pal(f"Se ha establecido conexión de forma exitosa con la Base de Datos: {dbname}")

        try:
            tester_id = int(input("\nIngrese el ID del tester: "))
            set_id = int(input("Ingrese el ID del SET de Pruebas: "))
            select = connection_string.cursor()

            script_progress = pal(f"Realizando consultas a la Base de Datos: {dbname}")

            global select_user
            select.execute("SELECT CONCAT(tester_name, ' ', tester_lastname, ' ', tester_m_lastname) FROM test.testers WHERE id = %s", (tester_id,))
            select_user = select.fetchone()[0]

            global select_test_set
            select.execute("SELECT test_set_code FROM test.test_sets WHERE id = %s AND active = true", (set_id,))
            select_test_set = select.fetchone()[0]

        except DatabaseError as de:
            print(f"Error en Consultas. No se pudieron extraer los datos: {de}")
        else:
            script_success = pal("Consultas realizadas con éxito. Extrayendo información de Inicio de Ejecución...")
            script_select_user = pal(f"Usuario que inicia la ejecución de Pruebas: {select_user}")
            script_select_test_set = pal(f"Set de Pruebas que será ejecutado: {select_test_set}")
        finally:
            select.close()
    finally:
        connection_string.close()

start_inputs()