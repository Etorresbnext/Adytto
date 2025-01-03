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

            global dropdown_configuration_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 16")
            dropdown_configuration_object_name = select.fetchone()[0]

            global btn_cities_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 17")
            btn_cities_object_name = select.fetchone()[0]

            global btn_customers_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 18")
            btn_customers_object_name = select.fetchone()[0]

            global btn_neighborhoods_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 19")
            btn_neighborhoods_object_name = select.fetchone()[0]

            global btn_driver_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 20")
            btn_driver_object_name = select.fetchone()[0]

            global btn_post_codes_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 21")
            btn_post_codes_object_name = select.fetchone()[0]

            global btn_sending_message_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 22")
            btn_sending_message_object_name = select.fetchone()[0]

            global btn_states_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 23")
            btn_states_object_name = select.fetchone()[0]

            global btn_question_forms_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 24")
            btn_question_forms_object_name = select.fetchone()[0]

            global btn_notifications_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 25")
            btn_notifications_object_name = select.fetchone()[0]

            global btn_organizations_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 26")
            btn_organizations_object_name = select.fetchone()[0]

            global btn_countries_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 27")
            btn_countries_object_name = select.fetchone()[0]

            global btn_questions_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 28")
            btn_questions_object_name = select.fetchone()[0]

            global btn_resources_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 29")
            btn_resources_object_name = select.fetchone()[0]

            global btn_types_licenses_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 30")
            btn_types_licenses_object_name = select.fetchone()[0]

            global btn_types_transport_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 31")
            btn_types_transport_object_name = select.fetchone()[0]

            global btn_transports_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 32")
            btn_transports_object_name = select.fetchone()[0]

            global btn_locations_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 33")
            btn_locations_object_name = select.fetchone()[0]

            global btn_users_object_name
            select.execute("SELECT name FROM test.web_objects WHERE id = 34")
            btn_users_object_name = select.fetchone()[0]







            global dropdown_configuration_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 16")
            dropdown_configuration_xpath_grouper = select.fetchone()[0]

            global btn_cities_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 17")
            btn_cities_xpath_grouper = select.fetchone()[0]

            global btn_customers_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 18")
            btn_customers_xpath_grouper = select.fetchone()[0]

            global btn_neighborhoods_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 19")
            btn_neighborhoods_xpath_grouper = select.fetchone()[0]

            global btn_driver_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 20")
            btn_driver_xpath_grouper = select.fetchone()[0]

            global btn_post_codes_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 21")
            btn_post_codes_xpath_grouper = select.fetchone()[0]

            global btn_sending_message_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 22")
            btn_sending_message_xpath_grouper = select.fetchone()[0]

            global btn_states_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 23")
            btn_states_xpath_grouper = select.fetchone()[0]

            global btn_question_forms_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 24")
            btn_question_forms_xpath_grouper = select.fetchone()[0]

            global btn_notifications_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 25")
            btn_notifications_xpath_grouper = select.fetchone()[0]

            global btn_organizations_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 26")
            btn_organizations_xpath_grouper = select.fetchone()[0]

            global btn_countries_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 27")
            btn_countries_xpath_grouper = select.fetchone()[0]

            global btn_questions_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 28")
            btn_questions_xpath_grouper = select.fetchone()[0]

            global btn_resources_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 29")
            btn_resources_xpath_grouper = select.fetchone()[0]

            global btn_types_licenses_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 30")
            btn_types_licenses_xpath_grouper = select.fetchone()[0]

            global btn_types_transport_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 31")
            btn_types_transport_xpath_grouper = select.fetchone()[0]

            global btn_transports_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 32")
            btn_transports_xpath_grouper = select.fetchone()[0]

            global btn_locations_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 33")
            btn_locations_xpath_grouper = select.fetchone()[0]

            global btn_users_xpath_grouper
            select.execute("SELECT xpath_grouper FROM test.web_objects WHERE id = 34")
            btn_users_xpath_grouper = select.fetchone()[0]


        except:
            print("Error en consulta")
        finally:
            select.close()
    finally:
        connection_string.close()

home_web_objects()