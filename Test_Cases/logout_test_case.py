from Libraries.libraries import webdriver
from Libraries.mkdir import image_logs_directory as ild
from Libraries.logs import print_action_logs as pal, get_image_action_date as giad, get_image_action_count as giac
from Page_Objects import login_objects as lo, home_objects as ho
from Database.db_inputs import db_login_inputs
from Libraries import global_variables as gv
from Libraries.global_variables import take_action_screenshot as tas
from Libraries.elapsed_time import test_case_start_date as start, test_case_end_date as end
from Database import db_urls
import Another_Test as AT
from Database.db_web_browsers.db_web_browser_info import get_browser_version as gbv


def close_web_site():
    if 2 in AT.test_cases_ids:
        print("\nHola Mundo 2")
        navegadores = AT.web_browsers_executions.get(2, [])[0]
        print(navegadores)
        nombres_navegadores = AT.web_browsers_names.get(2, [])[0]
        global start_date
        start_date = start()
        gv.info(" -------------- INICIO DE EJECUCIÓN ------------- ")
        gv.info(f" ---------- {start_date} ---------- \n")
        for j in range(len(navegadores)):
            browser_name = nombres_navegadores[j]
            browser_code = db_login_inputs.bc[j]
            gv.info(pal(f"Los Casos de Prueba serán ejecutados en el Navegador: {browser_name}"))
            driver = getattr(webdriver, navegadores[j])()
            browser_version = gbv(driver)
            gv.info(pal(f"Versión utilizada para el Navegador {browser_name}: {browser_version}"))
            driver.maximize_window()
            gv.info(pal(f"Preparandose para abrir el Portal Web {db_urls.login_url_name} con la url {db_urls.login_url} en el navegador {browser_name} {browser_version}"))
            driver.get(db_urls.login_url)
            gv.info(pal(f"Se ha abierto el Portal Web {db_urls.login_url_name} con la url {db_urls.login_url} con éxito \n"))
            tas(driver, f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} - {browser_code}.png")

            for i in range(db_login_inputs.tr):

                try:
                    txt_email = driver.find_element(*lo.txt_email_name)
                    txt_password = driver.find_element(*lo.txt_password_id)
                    btn_login = driver.find_element(*lo.btn_login_xpath)
                except:
                    gv.error(pal(f"No se pudieron localizar los elementos para cargar la página"))
                else:
                    try:
                        email = db_login_inputs.em[i]
                        gv.info(pal(f"Recopilando datos de entrada para Inicio de Sesión... Correo Electrónico: {db_login_inputs.em[i]}"))
                        password = db_login_inputs.passw[i]
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
                                    f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El valor {db_login_inputs.em[i]} ha sido capturado como correo electrónico en el campo {lo.txt_email_object_name}"))
                            tas(driver,f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} - {browser_code} - {db_login_inputs.em[i]}.png")

                        try:
                            txt_password.send_keys(password)
                        except:
                            print("Error PASS")
                        else:
                            gv.info(
                                pal(
                                    f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El valor {db_login_inputs.passw[i]} ha sido capturado como contraseña en el campo {lo.txt_password_object_name}"))
                            tas(driver, f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} - {browser_code} - {db_login_inputs.em[i]} - {db_login_inputs.passw[i]}.png")

                        try:
                            btn_login.click()
                        except:
                            print("Error Click")
                        else:
                            gv.info(
                                pal(
                                    f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic sobre el botón {lo.btn_login_object_name}"))
                            tas(driver, f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} - {browser_code} - {lo.btn_login_object_name}.png")
                finally:
                    gv.info(
                        pal(
                            f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Iniciando Sesión..."))

                try:
                    gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Inicio de Sesión Exito"))
                    home = gv.element_located(driver, *ho.btn_initials_id)
                except:
                    print("EQUIS DE")
                else:
                    gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se muestra la ventana {db_urls.home_url_name} en pantalla"))
                    tas(driver,f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} - {browser_code} - {db_urls.home_url_name}.png")
                try:
                    btn_initials = driver.find_element(*ho.btn_initials_id)
                except:
                    print("Se me acaban los carteles")
                else:
                    btn_initials.click()
                    gv.info(
                        pal(
                            f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic sobre el botón {ho.btn_initials_object_name}"))
                    tas(driver,f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} - {browser_code} - {ho.btn_initials_object_name}.png")
                try:
                    menu = gv.element_located(driver, *ho.card_initials_class)
                    gv.info(
                        pal(
                            f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se muestra en pantalla la tarjeta de usuario {ho.card_initials_object_name}"))
                    tas(driver,f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} - {browser_code} - {ho.card_initials_object_name}.png")
                except:
                    print("HM")


                try:
                    btn_logout = driver.find_element(*ho.btn_logout_xpath)
                except:
                    print("ª")
                else:
                    btn_logout.click()
                    tas(driver,f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} - {browser_code} - {ho.btn_logout_object_name}.png")
                    gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic sobre el botón {ho.btn_logout_object_name}"))

                try:
                    gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Cerrando Sesión... {ho.btn_logout_object_name}"))
                    login = gv.element_located(driver, *lo.txt_email_name)
                except:
                    print("Zy")
                else:
                    gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Cierre de Sesión Exitoso"))
                    driver.get(db_urls.login_url)
                    tas(driver,f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} - {browser_code} - {db_urls.login_url_name}.png")
                finally:
                    gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se actualiza el Portal Web {db_urls.login_url_name}"))

            gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Cerrando el Navegador..."))
            driver.quit()
            gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El Navegador ha sido cerrado con éxito \n"))
        global end_date
        end_date = end()
        gv.info(" --------------- FIN DE EJECUCIÓN --------------- ")
        gv.info(f" ---------- {end_date} ---------- \n")
        global elapsed
        elapsed = end_date - start_date
        gv.info(" -------- TIEMPO TRANSCURRIDO ------- ")
        gv.info(f" ---------- {elapsed} ---------- \n")
    else:
        print("\nNo se encuentra")