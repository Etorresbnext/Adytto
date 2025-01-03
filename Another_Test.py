from selenium import webdriver
from Database.db_connection import db_connection_func

def test_set_test_case():
    try:
        global test_cases_ids
        test_cases_ids = []
        global web_browsers_names
        web_browsers_names = {}
        global web_browsers_executions
        web_browsers_executions = {}
        input_test_set_id = int(input("\nIngrese el ID del Set de Pruebas: "))
        test_cases_quantity = int(input("¿Cuántos casos de Prueba se van a Ejecutar?: "))
        connection_string = db_connection_func()
    except:
        print("MAL")
    else:
        print("BIEN")

        for i in range(test_cases_quantity):
            input_test_case_id = int(input("\nIngrese el ID del Caso de Prueba a Ejecutar: "))
            input_browser_quantity = int(input("Ingrese en Cuántos Navegadores se Ejecutará el C.P: "))
            test_cases_ids.append(input_test_case_id)
            select = connection_string.cursor()

            global result
            select.execute("SELECT * FROM test.execute_test_cases(%s, %s, %s)", (input_test_set_id, input_test_case_id, input_browser_quantity,))
            result = select.fetchall()
            select.close()

            print("Opciones disponibles:")
            for j, k in enumerate(result, 1):
                inner_list = k[3]
                print(f"{j}. {inner_list}")

            input_browser_execution = int(input("¿En cuáles navegadores se ejecutaran los Casos de Prueba?: "))
            if 1 <= input_browser_execution <= len(result):
                browser_execution = result[input_browser_execution - 1][3]
                browser_name = result[input_browser_execution - 1][2]
                if input_test_case_id in web_browsers_executions:
                    web_browsers_executions[input_test_case_id].append(browser_execution)
                    web_browsers_names[input_test_case_id].append(browser_name)
                else:
                    web_browsers_executions[input_test_case_id] = [browser_execution]
                    web_browsers_names[input_test_case_id] = [browser_name]
                print(f"Para el Set de Pruebas '{result[0][0]}' se ejecutará el Caso de Prueba '{result[0][1]}' en el/los Navegador/es: '{browser_name}'")
            else:
                print("Horrible")

    finally:
        connection_string.close()

test_set_test_case()
print(web_browsers_executions)
print(web_browsers_names)


'''def test_set_test_case():
    try:
        global test_cases_ids
        test_cases_ids = []
        global web_browsers_executions
        web_browsers_executions = {}
        input_test_set_id = int(input("\nIngrese el ID del Set de Pruebas: "))
        test_cases_quantity = int(input("¿Cuántos casos de Prueba se van a Ejecutar?: "))
        connection_string = db_connection_func()
    except:
        print("MAL")
    else:
        print("BIEN")

        for i in range(test_cases_quantity):
            input_test_case_id = int(input("\nIngrese el ID del Caso de Prueba a Ejecutar: "))
            input_browser_quantity = int(input("Ingrese en Cuántos Navegadores se Ejecutará el C.P: "))
            test_cases_ids.append(input_test_case_id)
            select = connection_string.cursor()

            global result
            select.execute("SELECT * FROM test.select_webdrivers_from_test_sets_test_cases(%s, %s, %s)", (input_test_set_id, input_test_case_id, input_browser_quantity,))
            result = select.fetchall()
            select.close()

            print("Opciones disponibles:")
            for j, k in enumerate(result, 1):
                inner_list = k[0]
                print(f"{j}. {inner_list}")

            input_browser_execution = int(input("¿En cuáles navegadores se ejecutaran los Casos de Prueba?: "))
            if 1 <= input_browser_execution <= len(result):
                browser_execution = result[input_browser_execution - 1][0]
                if input_test_case_id in web_browsers_executions:
                    web_browsers_executions[input_test_case_id].append(browser_execution)
                else:
                    web_browsers_executions[input_test_case_id] = [browser_execution]
                print(f"Se ejecutará el Caso de Prueba en el/los Navegador/es: {browser_execution}")
            else:
                print("Horrible")


            if 1 <= input_browser_execution <= len(result):
                global browser_execution
                browser_execution = result[input_browser_execution - 1][0]
                web_browsers_executions.append(browser_execution)
                print(f"Se ejecutará el Caso de Prueba en el/los Navegador/es: {browser_execution}")
            else:
                print("Horrible")

            for i in range(len(browser_execution)):
                driver = getattr(webdriver, browser_execution[i])()
                driver.maximize_window()
                driver.get("https://www.google.com/")
                driver.quit()


    finally:
        print(test_cases_ids)
        print(web_browsers_executions)
        connection_string.close()'''