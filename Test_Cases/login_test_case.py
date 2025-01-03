from Libraries.libraries import webdriver
from Libraries.mkdir import image_logs_directory as ild
from Libraries.logs import print_action_logs as pal, get_image_action_date as giad, get_image_action_count as giac
from Page_Objects import login_objects as lo, home_objects as ho
from Database.db_inputs import db_login_inputs as dli
from Libraries import global_variables as gv
from Libraries.global_variables import take_action_screenshot as tas
from Libraries.elapsed_time import test_case_start_date as start, test_case_end_date as end
from Database import db_urls
from Database.db_web_browsers import db_set_web_browser_executions as gwb, db_web_browser_for_test_executions as wbe, \
    db_web_browser_info as wbi
from Database.db_web_browsers.db_web_browser_info import get_browser_version as gbv


def login_test_case_execution():
    start_date = start()
    gv.info(" -------------- INICIO DE EJECUCIÓN ------------- ")
    gv.info(f" ---------- {start_date} ---------- \n")

    for i in range(gwb.total_web_browsers):
        browser_name = wbi.web_browser_name[i]
        browser_code = wbi.web_browser_code[i]

        if wbe.login_execution[i] is True:
            driver = getattr(webdriver, wbi.web_browser_web_driver[i])()
            browser_version = gbv(driver)
            gv.info(pal(f"El Caso de Prueba será ejecutado en el Navegador {browser_name}"))
            login_test_case_flow(driver, browser_name, browser_version)
        else:
            gv.info(pal(f"El Caso de Prueba no será ejecutado en el Navegador {browser_name}"))

    end_date = end()
    gv.info(" --------------- FIN DE EJECUCIÓN --------------- ")
    gv.info(f" ---------- {end_date} ---------- \n")
    elapsed = end_date - start_date
    gv.info(" -------- TIEMPO TRANSCURRIDO ------- ")
    gv.info(f" ---------- {elapsed} ---------- \n")


def login_test_case_flow(driver, browser_name, browser_version):
    if 1 in gwb.test_cases_ids:
        driver.maximize_window()
        driver.get(db_urls.login_url)

        for i in range(dli.total_active_users):
            email = dli.user_information[i][0]
            password = dli.user_information[i][1]

            if login_general(driver, email, password, browser_name, browser_version):
                gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se muestra la ventana {db_urls.home_url_name} en pantalla"))
                tas(driver,f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {db_urls.home_url_name}.png")
                logout_general(driver, browser_name, browser_version)
            else:
                gv.error(pal(f"Fallo en el Inicio de Sesión con {email}"))

        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Cerrando el Navegador..."))
        driver.quit()
        gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El Navegador ha sido cerrado con éxito \n"))
    else:
        gv.info(pal("El Caso de Prueba no se encuentra activo"))


def login_general(driver, email, password, browser_name, browser_version):
    try:
        try:
            txt_email = gv.element_located(driver, *lo.txt_email_name)
        except:
            gv.error(pal(f"No se encontró el objeto {lo.txt_email_object_name}"))
        try:
            txt_password = gv.element_located(driver, *lo.txt_password_id)
        except:
            gv.error(pal(f"No se encontró el objeto {lo.txt_password_object_name}"))
        try:
            btn_login = gv.element_located(driver, *lo.btn_login_xpath)
        except:
            gv.error(pal(f"No se encontró el objeto {lo.btn_login_object_name}"))
    except Exception as e:
        gv.error(pal(f"Ha ocurrido un error durante el inicio de Sesión: {str(e)}"))
        return False
    else:
        try:
            gv.info(pal(f"Recopilando datos de entrada para Inicio de Sesión... Correo Electrónico: {email}"))
            gv.info(pal(f"Recopilando datos de entrada para Inicio de Sesión... Contraseña: {password}"))

            txt_email.send_keys(email)
            gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El valor {email} ha sido capturado como correo electrónico en el campo {lo.txt_email_object_name}"))
            tas(driver, f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {email}.png")

            txt_password.send_keys(password)
            gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: El valor {password} ha sido capturado como contraseña en el campo {lo.txt_password_object_name}"))
            tas(driver, f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {email} - {password}.png")

            btn_login.click()
            gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se ha dado clic sobre el botón {lo.btn_login_object_name}"))

            gv.element_located(driver, *ho.btn_initials_id)
            gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Inicio de Sesión Exitoso"))
            return True
        except:
            gv.error(pal("Ha ocurrido un error inesperado"))


def logout_general(driver, browser_name, browser_version):
    try:
        btn_initials = driver.find_element(*ho.btn_initials_id)
        btn_initials.click()
        tas(driver,
            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {ho.btn_initials_object_name}.png")

        gv.element_located(driver, *ho.card_initials_class)
        tas(driver,
            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {ho.card_initials_object_name}.png")

        btn_logout = driver.find_element(*ho.btn_logout_xpath)
        btn_logout.click()
        tas(driver,
            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {ho.btn_logout_object_name}.png")

        gv.info(
            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Cierre de Sesión Exitoso"))
        driver.get(db_urls.login_url)
        tas(driver,
            f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} -  - {db_urls.login_url_name}.png")
        gv.info(
            pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Se actualiza el Portal Web {db_urls.login_url_name}"))

    except Exception as e:
        gv.error(pal(f"Error durante el cierre de sesión: {str(e)}"))

