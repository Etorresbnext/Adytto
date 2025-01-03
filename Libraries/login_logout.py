def perform_login(driver, email, password):
    try:
        txt_email = gv.element_located(driver, *lo.txt_email_name)
        txt_password = gv.element_located(driver, *lo.txt_password_id)
        btn_login = gv.element_located(driver, *lo.btn_login_xpath)
    except:
        gv.error(pal("No se pudieron localizar los elementos para cargar la página"))
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
            tas(driver, f"{ild()}/{str(next(giac())).zfill(3)} - {giad()} - {browser_name} - - {lo.btn_login_object_name}.png")

            gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Iniciando Sesión..."))

            home = gv.element_located(driver, *ho.btn_initials_id)
            gv.info(pal(f"[Navegador: {browser_name}] [Versión del Navegador: {browser_version}]:: Inicio de Sesión Exitoso"))
            return True
        except:
            gv.error(pal("Error durante el inicio de sesión"))
            return False