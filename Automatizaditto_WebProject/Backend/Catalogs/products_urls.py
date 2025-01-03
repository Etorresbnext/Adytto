from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls

connection_string = fl.db_connection_func()


def insert_new_url():
    validity_errors = {}

    url_name = fl.request.form['urlName']
    if not url_name or not url_name.strip():
        validity_errors['nullName'] = 'Asegúrese de capturar un nombre para la URL. Este campo es requerido.'

    url_protocol = fl.request.form['urlProtocol']
    if not url_protocol or not url_protocol.strip():
        validity_errors['nullProtocol'] = 'Seleccione un protócolo.'

    url_domain = fl.request.form['urlDomain']
    if not url_domain or not url_domain.strip():
        validity_errors['nullDomain'] = 'Capture el dominio para la URL.'

    try:
        fl.ipaddress.ip_address(url_domain)
    except ValueError:
        validity_errors['invalidIp'] = 'La dirección IP no es válida.'

    url_port = fl.request.form['urlPort']
    if not url_port or not url_port.strip():
        validity_errors['nullPort'] = 'Capture el puerto.'

    url_path = fl.request.form['urlPath']
    if not url_path or not url_path.strip():
        validity_errors['nullPath'] = 'Capture la ruta.'

    url_product = fl.request.form['urlProduct']
    if not url_protocol or not url_product.strip():
        validity_errors['nullProduct'] = 'Seleccione el producto al que pertenece la URL.'

    url_env = fl.request.form['urlEnv']
    if not url_env or not url_env.strip():
        validity_errors['nullEnv'] = 'Seleccione el ambiente en el que se encuentra la URL.'

    url_separator = ':'
    url_slug = '/'
    url_full = url_protocol + url_domain + url_separator + url_port + url_slug

    if validity_errors:
        return fl.jsonify(validity_errors), 404

    try:
        insert = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        insert.execute(sql.insert_url, (url_name, url_full, url_path, url_product, url_env, fl.session['user_id'],))
        connection_string.commit()
        insert.close()
        return fl.jsonify({'redirect_url': fl.url_for('render_page', page_name=urls(8))})
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500


def update_url():
    update_url_id = fl.request.form['updateID_hidden']
    update_url_name = fl.request.form['updateURLName']
    update_url_domain = fl.request.form['updateUrlDomain']
    update_url_port = fl.request.form['updateUrlPort']
    update_url_path = fl.request.form['updateUrlPath']
    update_url_env = fl.request.form['updateUrlEnv']
    update_url_product = fl.request.form['updateUrlProduct']
    update_url_protocol = fl.request.form['updateUrlProtocol']
    update_url_separator = ':'
    update_url_slug = '/'
    update_url_full = update_url_protocol + update_url_domain + update_url_separator + update_url_port + update_url_slug

    try:
        if not update_url_name or not update_url_name.strip():
            return fl.jsonify({'message': 'Error al Actualizar. Debe capturar un nombre para la URL'}), 404
        if not update_url_domain or not update_url_domain.strip():
            return fl.jsonify(({'message': 'Error al Actualizar. Debe capturar un dominio para la URL'})), 404
        if not update_url_port or not update_url_port.strip():
            return fl.jsonify(({'message': 'Error al Actualizar. Debe capturar un puerto'})), 404
        if not update_url_path or not update_url_path.strip():
            return fl.jsonify(({'message': 'Error al Actualizar. Debe capturar una ruta para la URL'})), 404
        else:
            try:
                update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
                update.execute(sql.update_url, (
                    update_url_id, update_url_name, update_url_full, update_url_path, update_url_product,
                    update_url_env,
                    fl.session['user_id'],))
                connection_string.commit()
                update.close()
                return fl.redirect(fl.url_for('render_page', page_name=urls(8)))
            except Exception as e:
                return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos', 'error': str(e)}), 500
