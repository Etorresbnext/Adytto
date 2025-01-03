from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls

connection_string = fl.db_connection_func()


def insert_new_operative_system():
    validity_errors = {}

    os_family = fl.request.form['osFamily']
    if not os_family or not os_family.strip():
        validity_errors['nullFamily'] = 'Asegúrese de seleccionar la Familia del Sistema Operativo.'

    os_name = fl.request.form['osName']
    if not os_name or not os_name.strip():
        validity_errors['nullName'] = 'Asegúrese de capturar un nombre para el Sistema Operativo.'

    os_edition = fl.request.form['osEdition']
    if not os_edition or not os_edition.strip():
        validity_errors['nullEdition'] = 'Asegúrese de capturar la edición del Sistema Operativo.'

    os_version = fl.request.form['osVersion']
    if not os_version or not os_version.strip():
        validity_errors['nullVersion'] = 'Asegúrese de capturar la versión del Sistema Operativo.'

    os_architecture = fl.request.form['osArch']
    if not os_architecture or not os_architecture.strip():
        validity_errors['nullArch'] = 'Asegúrese de seleccionar la arquitectura del Sistema Operativo.'

    if validity_errors:
        return fl.jsonify(validity_errors), 404

    try:
        insert = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        insert.execute(sql.insert_operative_system,
                       (os_family, os_name, os_edition, os_version, os_architecture, fl.session['user_id'],))
        connection_string.commit()
        insert.close()
        return fl.jsonify({'redirect_url': fl.url_for('render_page', page_name=urls(14))}), 200
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500


def update_operative_system():
    update_os_id = fl.request.form['updateID_hidden']
    update_os_family = fl.request.form['updateOsFamily']
    update_os_name = fl.request.form['updateOsName']
    update_os_edition = fl.request.form['updateOsEdition']
    update_os_version = fl.request.form['updateOsVersion']
    update_os_architecture = fl.request.form['updateOsArch']

    try:
        update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        update.execute(sql.update_operative_system, (
        update_os_id, update_os_family, update_os_name, update_os_edition, update_os_version, update_os_architecture,
        fl.session['user_id'],))
        connection_string.commit()
        update.close()
        return fl.redirect(fl.url_for('render_page', page_name=urls(14)))
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500
