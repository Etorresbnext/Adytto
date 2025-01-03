from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls

connection_string = fl.db_connection_func()


def insert_new_hardware_configuration():
    validity_errors = {}

    hc_name = fl.request.form['hcName']
    if not hc_name or not hc_name.strip():
        validity_errors['nullName'] = 'Asegúrese de capturar un nombre para la Configuración de Hardware'

    hc_desc = fl.request.form['hcDesc']

    hc_processor = fl.request.form['hcProcessor']
    if not hc_processor or not hc_processor.strip():
        validity_errors['nullProcessor'] = 'Seleccione un procesador para la Configuración de Hardware'

    hc_hard_drive = fl.request.form['hcHardDrive']
    if not hc_hard_drive or not hc_hard_drive.strip():
        validity_errors['nullHardDrive'] = 'Seleccione un disco duro para la Configuración de Hardware'

    hc_ram = fl.request.form['hcRam']
    if not hc_ram or not hc_ram.strip():
        validity_errors['nullRam'] = 'Seleccione una Memoria RAM para la Configuración de Hardware'

    redirect = fl.request.form.get('redirect')

    if validity_errors:
        return fl.jsonify(validity_errors), 404

    try:
        insert = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        insert.execute(sql.insert_hard_conf, (hc_name, hc_desc, hc_processor, hc_hard_drive, hc_ram, fl.session['user_id'],))
        insert_id = insert.fetchone()['insert_new_hardware_configuration']
        connection_string.commit()
        insert.close()
        if not redirect:
            return fl.redirect(fl.url_for('render_page', page_name=urls(12)))
        else:
            return fl.jsonify({'success': True, 'Id': insert_id, 'Name': hc_name, 'description': hc_desc})
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500


def update_hardware_configuration():
    update_hc_id = fl.request.form['updateID_hidden']
    update_hc_name = fl.request.form['updateHcName']
    update_hc_desc = fl.request.form['updateHcDesc']
    update_hc_processor = fl.request.form['updateHcProcessor']
    update_hc_hard_drive = fl.request.form['updateHcHardDrive']
    update_hc_ram = fl.request.form['updateHcRam']

    try:
        update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        update.execute(sql.update_hard_conf, (update_hc_id, update_hc_name, update_hc_desc, update_hc_processor, update_hc_hard_drive, update_hc_ram, fl.session['user_id'],))
        connection_string.commit()
        update.close()
        return fl.redirect(fl.url_for('render_page', page_name=urls(12)))
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500
