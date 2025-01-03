from Database.db_connection import db_connection_func
from Libraries.logs import print_action_logs as pal
from psycopg2 import OperationalError, DatabaseError

def login_web_objects():
    try:
        objects_quantity = int(input("\nIngrese la cantidad de objetos que se van a extraer: "))
        list_objects_names = []
        list_objects_id_grouper = []
        list_objects_name_grouper = []
        list_objects_class_grouper = []
        list_objects_xpath_grouper = []
        connection_string = db_connection_func()
        global login_web_objects_info
        login_web_objects_info_list = []
    except:
        print("MAL")
    else:

        select = connection_string.cursor()

        select.execute("SELECT * FROM test.select_login_web_objects()")
        login_web_objects_list = select.fetchall()

        print("\nObjetos disponibles para la página Login")
        for j in login_web_objects_list:
            print(f"[{j[0]:<2}  |   {j[1]:<27}]")

        for i in range(objects_quantity):
            input_object_id = int(input(f"\nIngrese el ID del Objeto {i+1}: "))

            select.execute("SELECT * FROM test.get_object_name(%s)", (input_object_id,))
            web_object_name = select.fetchone()[0]
            list_objects_names.append(web_object_name)

            select.execute("SELECT * FROM test.get_object_id_grouper(%s)", (input_object_id,))
            web_object_id_grouper = select.fetchone()[0]
            list_objects_id_grouper.append(web_object_id_grouper)

            select.execute("SELECT * FROM test.get_object_name_grouper(%s)", (input_object_id,))
            web_object_name_grouper = select.fetchone()[0]
            list_objects_name_grouper.append(web_object_name_grouper)

            select.execute("SELECT * FROM test.get_object_class_grouper(%s)", (input_object_id,))
            web_object_class_grouper = select.fetchone()[0]
            list_objects_class_grouper.append(web_object_class_grouper)

            select.execute("SELECT * FROM test.get_object_xpath_grouper(%s)", (input_object_id,))
            web_object_xpath_grouper = select.fetchone()[0]
            list_objects_xpath_grouper.append(web_object_xpath_grouper)

            login_web_objects_info_list.append(web_object_name)

        login_web_objects_info = pal(f"Se ha extraido la información de los objetos: '{login_web_objects_info_list}'")


        select.close()

    finally:
        connection_string.close()

    return list_objects_names, list_objects_id_grouper, list_objects_name_grouper, list_objects_class_grouper, list_objects_xpath_grouper