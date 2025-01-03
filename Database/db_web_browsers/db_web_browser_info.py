from Database.db_connection import db_connection_func
from Libraries.logs import print_action_logs as pal
from psycopg2 import OperationalError, DatabaseError

def get_browsers_information():
    try:
        connection_string = db_connection_func()
        dbname = connection_string.info.dbname
        global script_progress, script_success, script_web_browser_name, script_web_browser_code, script_web_browser_web_driver
    except OperationalError as oe:
        print(f"{oe}")
    else:

        select = connection_string.cursor()
        script_progress = pal(f"Realizando consultas a la Base de Datos: {dbname}")

        global web_browser_name
        select.execute("SELECT name FROM test.web_browsers WHERE active = true ORDER BY id ASC")
        select_web_browser_name = select.fetchall()
        web_browser_name = [i[0] for i in select_web_browser_name]

        global web_browser_code
        select.execute("SELECT code FROM test.web_browsers WHERE active = true ORDER BY id ASC")
        select_web_browser_code = select.fetchall()
        web_browser_code = [i[0] for i in select_web_browser_code]

        global web_browser_web_driver
        select.execute("SELECT web_driver FROM test.web_browsers WHERE active = true ORDER BY id ASC")
        select_web_browser_web_driver = select.fetchall()
        web_browser_web_driver = [i[0] for i in select_web_browser_web_driver]

        select.close()

        script_success = pal("Consultas realizadas con éxito. Extrayendo información de los Navegadores...")
        script_web_browser_name = pal(f"Navegadores Activos y No Borrados disponibles: {web_browser_name}")
        script_web_browser_code = pal(f"Códigos de los Navegadores: {web_browser_code}")
        script_web_browser_web_driver = pal(f"Web Drivers de los Navegadores {web_browser_web_driver}")
    finally:
        connection_string.close()

get_browsers_information()

def get_browser_version(driver):
    browser_version = driver.capabilities.get('browserVersion', driver.capabilities.get('version'))
    return browser_version