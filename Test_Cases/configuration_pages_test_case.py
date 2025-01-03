import time
from Libraries.libraries import webdriver
from Libraries.mkdir import image_logs_directory as ild
from Libraries.logs import print_action_logs as pal, get_image_action_date as giad, get_image_action_count as giac
from Page_Objects import login_objects as lo, home_objects as ho, configuration_objects as co
from Database.db_inputs import db_login_inputs as dli
from Libraries import global_variables as gv
from Libraries.global_variables import take_action_screenshot as tas
from Libraries.elapsed_time import test_case_start_date as start, test_case_end_date as end
from Database import db_urls
from Database.db_web_browsers import db_set_web_browser_executions as gwb, db_web_browser_for_test_executions as wbe, db_web_browser_info as wbi
from Database.db_web_browsers.db_web_browser_info import get_browser_version as gbv
from Test_Cases.login_test_case import login_general, logout_general


def executions():
    for i in range(gwb.total_web_browsers):
        def web_browser_execution():
            global browser_name
            browser_name = wbi.web_browser_name[i]
            global browser_code
            browser_code = wbi.web_browser_code[i]
            if wbe.config_execution[i] is True:
                global driver
                driver = getattr(webdriver, wbi.web_browser_web_driver[i])()
                global browser_version
                browser_version = gbv(driver)
                print(f"El C.P. se ejecutará en {browser_name}")
                open_configuration_pages()
            else:
                print(f"El C.. no se ejecutará en {browser_name}")

        web_browser_execution()

def open_configuration_pages():
    if 3 in gwb.test_cases_ids:
        driver.maximize_window()
        driver.get(db_urls.login_url)
        for i in range(dli.total_active_users):

            try:
                txt_email = driver.find_element(*lo.txt_email_name)
                txt_password = driver.find_element(*lo.txt_password_id)
                btn_login = driver.find_element(*lo.btn_login_xpath)
            except:
                gv.error(pal(f"No se pudieron localizar los elementos para cargar la página"))
            else:
                try:
                    email = dli.user_information[i][0]
                    gv.info(
                        pal(f"Recopilando datos de entrada para Inicio de Sesión... Correo Electrónico: {email}"))
                    password = dli.user_information[i][1]
                    gv.info(pal(f"Recopilando datos de entrada para Inicio de Sesión... Contraseña: {password}"))
                except:
                    gv.error(pal("No se han podido recopilar los datos de entrada para el Inicio de Sesión"))
                else:
                    try:
                        txt_email.send_keys(email)
                    except:
                        print("Error")
                    else:
                        gv.info(
                            pal(
                                f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El valor {email} ha sido capturado como correo electrónico en el campo {lo.txt_email_object_name}"))
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {email}.png")

                    try:
                        txt_password.send_keys(password)
                    except:
                        print("Error PASS")
                    else:
                        gv.info(
                            pal(
                                f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El valor {password} ha sido capturado como contraseña en el campo {lo.txt_password_object_name}"))
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {email} - {password}.png")

                    try:
                        btn_login.click()
                    except:
                        print("Error Click")
                    else:
                        gv.info(
                            pal(
                                f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic sobre el botón {lo.btn_login_object_name}"))
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} - - {lo.btn_login_object_name}.png")
            finally:
                gv.info(
                    pal(
                        f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Iniciando Sesión..."))

            try:
                gv.info(
                    pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Inicio de Sesión Exito"))
                home = gv.element_located(driver, *ho.btn_initials_id)
            except:
                print("EQUIS DE")
            else:
                gv.info(
                    pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se muestra la ventana {db_urls.home_url_name} en pantalla"))
                tas(driver,
                    f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {db_urls.home_url_name}.png")

                gv.info(
                    pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.dropdown_configuration_object_name}"))
                if dli.user_information[i][3] is True:
                    btn_configuration = driver.find_element(*co.dropdown_configuration_xpath_grouper)
                    gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Objeto {co.dropdown_configuration_object_name} encontrado"))
                    btn_configuration.click()
                    gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: se ha dado clic sobre el menú {co.dropdown_configuration_object_name}"))
                    #gv.element_located(driver, *co.btn_customers_xpath_grouper)
                    try:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_cities_object_name}"))
                        btn_cities = gv.btn_located(driver, *co.btn_cities_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_cities_object_name} no se encuentra activo"))
                    else:
                        btn_cities.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_cities_object_name}.png")
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_cities_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_customers_object_name}"))
                        btn_customers = gv.btn_located(driver, *co.btn_customers_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_customers_object_name} no se encuentra activo"))
                    else:
                        btn_customers.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_customers_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_customers_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_neighborhoods_object_name}"))
                        btn_neighborhoods = gv.btn_located(driver, *co.btn_neighborhoods_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_neighborhoods_object_name} no se encuentra activo"))
                    else:
                        btn_neighborhoods.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_neighborhoods_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_neighborhoods_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_driver_object_name}"))
                        btn_driver = gv.btn_located(driver, *co.btn_driver_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_driver_object_name} no se encuentra activo"))
                    else:
                        btn_driver.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_driver_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_driver_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_post_codes_object_name}"))
                        btn_post_codes = gv.btn_located(driver, *co.btn_post_codes_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_post_codes_object_name} no se encuentra activo"))
                    else:
                        btn_post_codes.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_post_codes_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_post_codes_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_sending_message_object_name}"))
                        btn_sending_message = gv.btn_located(driver, *co.btn_sending_message_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_sending_message_object_name} no se encuentra activo"))
                    else:
                        btn_sending_message.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_sending_message_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_sending_message_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_states_object_name}"))
                        btn_states = gv.btn_located(driver, *co.btn_states_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_states_object_name} no se encuentra activo"))
                    else:
                        btn_states.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_states_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_states_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_question_forms_object_name}"))
                        btn_question_forms = gv.btn_located(driver, *co.btn_question_forms_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_question_forms_object_name} no se encuentra activo"))
                    else:
                        btn_question_forms.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_question_forms_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_question_forms_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_notifications_object_name}"))
                        btn_notifications = gv.btn_located(driver, *co.btn_notifications_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_notifications_object_name} no se encuentra activo"))
                    else:
                        btn_notifications.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_notifications_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_notifications_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_organizations_object_name}"))
                        btn_organizations = gv.btn_located(driver, *co.btn_organizations_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_organizations_object_name} no se encuentra activo"))
                    else:
                        btn_organizations.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_organizations_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_organizations_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_countries_object_name}"))
                        btn_countries = gv.btn_located(driver, *co.btn_countries_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_countries_object_name} no se encuentra activo"))
                    else:
                        btn_countries.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_countries_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_countries_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_questions_object_name}"))
                        btn_questions = gv.btn_located(driver, *co.btn_questions_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_questions_object_name} no se encuentra activo"))
                    else:
                        btn_questions.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_questions_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_questions_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_resources_object_name}"))
                        btn_resources = gv.btn_located(driver, *co.btn_resources_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_resources_object_name} no se encuentra activo"))
                    else:
                        btn_resources.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_resources_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_resources_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_types_licenses_object_name}"))
                        btn_types_licenses = gv.btn_located(driver, *co.btn_types_licenses_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_types_licenses_object_name} no se encuentra activo"))
                    else:
                        btn_types_licenses.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_types_licenses_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_types_licenses_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_types_transport_object_name}"))
                        btn_types_transport = gv.btn_located(driver, *co.btn_types_transport_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_types_transport_object_name} no se encuentra activo"))
                    else:
                        btn_types_transport.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_types_transport_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_types_transport_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_transports_object_name}"))
                        btn_transports = gv.btn_located(driver, *co.btn_transports_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_transports_object_name} no se encuentra activo"))
                    else:
                        btn_transports.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_transports_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_transports_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_locations_object_name}"))
                        btn_locations = gv.btn_located(driver, *co.btn_locations_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_locations_object_name} no se encuentra activo"))
                    else:
                        btn_locations.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_locations_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_locations_object_name}"))
                        time.sleep(5)

                    try:
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Buscando objeto: {co.btn_users_object_name}"))
                        btn_users = gv.btn_located(driver, *co.btn_users_xpath_grouper)
                    except:
                        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.btn_users_object_name} no se encuentra activo"))
                    else:
                        btn_users.click()
                        tas(driver,
                            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {co.btn_users_object_name}.png")
                        gv.info(
                            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic al botón {co.btn_users_object_name}"))
                        time.sleep(5)


                else:
                    gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El objeto {co.dropdown_configuration_object_name} no se encuentra"))

            try:
                btn_initials = driver.find_element(*ho.btn_initials_id)
            except:
                print("Se me acaban los carteles")
            else:
                btn_initials.click()
                gv.info(
                    pal(
                        f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic sobre el botón {ho.btn_initials_object_name}"))
                tas(driver,
                    f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {ho.btn_initials_object_name}.png")
            try:
                menu = gv.element_located(driver, *ho.card_initials_class)
                gv.info(
                    pal(
                        f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se muestra en pantalla la tarjeta de usuario {ho.card_initials_object_name}"))
                tas(driver,
                    f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {ho.card_initials_object_name}.png")
            except:
                print("HM")

            try:
                btn_logout = driver.find_element(*ho.btn_logout_xpath)
            except:
                print("ª")
            else:
                btn_logout.click()
                tas(driver,
                    f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {ho.btn_logout_object_name}.png")
                gv.info(
                    pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic sobre el botón {ho.btn_logout_object_name}"))

            try:
                gv.info(
                    pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Cerrando Sesión... {ho.btn_logout_object_name}"))
                login = gv.element_located(driver, *lo.txt_email_name)
            except:
                print("Zy")
            else:
                gv.info(
                    pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Cierre de Sesión Exitoso"))
                driver.get(db_urls.login_url)
                tas(driver,
                    f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {db_urls.login_url_name}.png")
            finally:
                gv.info(
                    pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se actualiza el Portal Web {db_urls.login_url_name}"))

        gv.info(
            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Cerrando el Navegador..."))
        driver.quit()
        gv.info(
            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El Navegador ha sido cerrado con éxito \n"))