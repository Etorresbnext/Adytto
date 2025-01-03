from Database.db_connection import db_connection_func
from Libraries.logs import print_action_logs as pal
from psycopg2 import OperationalError, DatabaseError

def select_browser_for_test_execution():
    try:
        global test_cases_ids
        test_cases_ids = []
        connection_string = db_connection_func()
    except:
        print("MALO MALISIMO")
    else:

        select = connection_string.cursor()

        global total_web_browsers
        select.execute("SELECT COUNT(*) FROM test.web_browsers")
        total_web_browsers = select.fetchone()[0]

        select.execute("SELECT name FROM test.web_browsers")
        select_web_browsers_names = select.fetchall()
        web_browsers_names = [i[0] for i in select_web_browsers_names]

        select.execute("SELECT COUNT(*) FROM test.test_cases WHERE active = true")
        total_active_test_cases = select.fetchone()[0]

        select.execute("SELECT * FROM test.select_active_test_cases()")
        select_test_cases_names = select.fetchall()
        test_cases_names = [i[0] for i in select_test_cases_names]

        for i in range(total_active_test_cases):
            select.execute("SELECT * FROM test.get_test_case_id(%s)", (test_cases_names[i],))
            test_case_id = select.fetchone()[0]
            test_cases_ids.append(test_case_id)
            for j in range(total_web_browsers):
                global web_browsers_executions
                select.execute("SELECT * FROM test.select_browser_execution_columns()")
                select_web_browsers_executions = select.fetchall()
                web_browsers_executions = [k[0] for k in select_web_browsers_executions]
                while True:
                    update = connection_string.cursor()
                    select_web_browser = input(f"\n¿Desea ejecutar el Caso de Prueba {test_cases_names[i]} en el Navegador {web_browsers_names[j]}? (S/N): ").strip().upper()
                    if select_web_browser in ['S', 'N']:
                        if select_web_browser == 'S':
                            print(f"Se ejecutaran las pruebas para el Navegador {web_browsers_names[j]}")
                            update.execute(f"UPDATE test.test_sets_test_cases SET {web_browsers_executions[j]} = true WHERE test_case_uuid = (SELECT uuid FROM test.test_cases WHERE name = '{test_cases_names[i]}')")
                            connection_string.commit()
                        else:
                            print(f"No se ejecutaran pruebas en el Navegador {web_browsers_names[j]}")
                            update.execute(f"UPDATE test.test_sets_test_cases SET {web_browsers_executions[j]} = false WHERE test_case_uuid = (SELECT uuid FROM test.test_cases WHERE name = '{test_cases_names[i]}')")
                            connection_string.commit()
                        break
                    else:
                        print("Ingrese S para Sí o No para No")
                    update.close()
            global result
            select.execute("SELECT * FROM  test.get_browsers_for_test_execution(%s)", (test_cases_ids[i],))
            result = select.fetchone()

    finally:
        connection_string.close()

select_browser_for_test_execution()