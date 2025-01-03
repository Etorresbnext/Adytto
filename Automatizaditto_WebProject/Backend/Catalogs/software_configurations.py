from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls

connection_string = fl.db_connection_func()


def insert_new_software_configuration():
    validity_errors = {}

    sc_name = fl.request.form['scName']
    if not sc_name or not sc_name.strip():
        validity_errors['nullName'] = 'Asegúrese de capturar un nombre para la Configuración de Software'

    sc_desc = fl.request.form['scDesc']

    sc_operative_system = fl.request.form['scOpSys']
    if not sc_operative_system or not sc_operative_system.strip():
        validity_errors['nullOs'] = 'Seleccione un sistema operativo para la Configuración de Software'

    redirect = fl.request.form.get('redirect')

    if validity_errors:
        return fl.jsonify(validity_errors), 404

    try:
        insert = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        insert.execute(sql.insert_soft_conf, (sc_name, sc_desc, sc_operative_system, fl.session['user_id'],))
        insert_id = insert.fetchone()['insert_new_software_configuration']
        connection_string.commit()
        insert.close()
        if not redirect:
            return fl.redirect(fl.url_for('render_page', page_name=urls(15)))
        else:
            return fl.jsonify({'success': True, 'Id': insert_id, 'Name': sc_name, 'description': sc_desc})
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500


def update_software_configuration():
    update_sc_id = fl.request.form['updateID_hidden']
    update_sc_name = fl.request.form['updateScName']
    update_sc_description = fl.request.form['updateScDesc']
    update_sc_operative_system = fl.request.form['updateScOpSys']

    try:
        update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        update.execute(sql.update_soft_conf, (update_sc_id, update_sc_name, update_sc_description, update_sc_operative_system, fl.session['user_id'],))
        connection_string.commit()
        update.close()
        return fl.redirect(fl.url_for('render_page', page_name=urls(15)))
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500

