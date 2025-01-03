from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls

connection_string = fl.db_connection_func()


def insert_new_runner():

    validity_errors = {}

    runner_name = fl.request.form['runnerName']
    if not runner_name or not runner_name.strip():
        validity_errors['nullName'] = 'Asegúrese de capturar un nombre para el Equipo'

    runner_desc = fl.request.form['runnerDesc']

    runner_ip = fl.request.form['runnerIp']
    if not runner_ip or not runner_ip.strip():
        validity_errors['nullIp'] = 'Asegúrese de capturar una dirección Ip para el Equipo.'

    try:
        fl.ipaddress.ip_address(runner_ip)
    except ValueError:
        validity_errors['invalidIp'] = 'La dirección IP no es válida.'

    runner_hard_conf = fl.request.form['runnerHardConfId']
    if not runner_hard_conf or not runner_hard_conf.strip():
        validity_errors['nullHardConf'] = 'Asegúrese de seleccionar una configuración de hardware para el Equipo.'

    runner_soft_conf = fl.request.form['runnerSoftConfId']
    if not runner_soft_conf or not runner_soft_conf.strip():
        validity_errors['nullSoftConf'] = 'Asegúrese de seleccionar una configuración de software para el Equipo.'

    if validity_errors:
        return fl.jsonify(validity_errors), 404

    try:
        insert = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        insert.execute(sql.insert_runner, (
            runner_name, runner_desc, runner_ip, runner_hard_conf, runner_soft_conf, fl.session['user_id']))
        connection_string.commit()
        insert.close()
        return fl.jsonify({'redirect_url': fl.url_for('render_page', page_name=urls(9))}), 200
    except Exception as e:
        connection_string.rollback()
        full_error = str(e)
        message_error = full_error.split("\n")[0]
        validity_errors['dbError'] = message_error
        return fl.jsonify(validity_errors), 500
        #return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500


def update_runner():
    update_runner_id = fl.request.form['updateID_hidden']
    update_runner_name = fl.request.form['updateRunnerName']
    update_runner_desc = fl.request.form['updateRunnerDesc']
    update_runner_ip = fl.request.form['updateRunnerIp']
    update_runner_hard_conf = fl.request.form['updateRunnerHardConf']
    update_runner_soft_conf = fl.request.form['updateRunnerSoftConf']

    try:
        fl.ipaddress.ip_address(update_runner_ip)
    except ValueError:
        return fl.jsonify({'messgae': 'La dirección IP no es válida.'}), 400

    try:
        if not update_runner_name or not update_runner_name.strip():
            return fl.jsonify({'message': 'Debe capturar un nombre para el Equipo'}), 404
        elif not update_runner_ip or not update_runner_ip.strip():
            return fl.jsonify(({'message': 'Debe capturar la dirección IP del Equipo'})), 404
        else:
            try:
                update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
                update.execute(sql.update_runner, (
                    update_runner_id, update_runner_name, update_runner_desc, update_runner_ip, update_runner_hard_conf,
                    update_runner_soft_conf, fl.session['user_id'],))
                connection_string.commit()
                update.close()
                return fl.redirect(fl.url_for('render_page', page_name=urls(9)))
            except Exception as e:
                return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos', 'error': str(e)}), 500


def verify_hardware_configuration():
    validity_errors = {}

    processor_id = fl.request.form['verifyHcProcessor']
    if not processor_id or not processor_id.strip():
        validity_errors['processorNull'] = 'Asegúrese de seleccionar un procesador de la lista.'

    hard_drive_id = fl.request.form['verifyHcHardDrive']
    if not hard_drive_id or not hard_drive_id.strip():
        validity_errors['hardDriveNull'] = 'Asegúrese de seleccionar un disco duro de la lista.'

    ram_id = fl.request.form['verifyHcRam']
    if not ram_id or not ram_id.strip():
        validity_errors['ramNull'] = 'Asegúrese de seleccionar una memoria ram de la lista.'

    if validity_errors:
        return fl.jsonify(validity_errors), 404

    try:
        select = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        select.execute(sql.select_verify_hard_conf, (processor_id, hard_drive_id, ram_id,))
        exists = select.fetchone()
        select.close()
        print(exists)

        if exists is None:
            return fl.jsonify({'exists': 0})

        if exists['Borrado'] is True:
            return fl.jsonify({'erased': 'El registro se encuentra borrado'}), 404
        elif exists['Borrado'] is False:
            return fl.jsonify({'exists': 1, 'data': exists})

    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500


def verify_software_configuration():
    validity_errors = {}

    os_id = fl.request.form['scOpSys']
    if not os_id or not os_id.strip():
        validity_errors['nullOs'] = 'Asegúrese de seleccionar un Sistema Operativo de la lista.'

    if validity_errors:
        return fl.jsonify(validity_errors), 404

    try:
        select = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        select.execute(sql.select_verify_soft_conf, (os_id,))
        exists = select.fetchone()
        select.close()
        print(exists)

        if exists is None:
            return fl.jsonify({'exists': 0})

        if exists['Borrado'] is True:
            return fl.jsonify({'erased': 'El registro se encuentra borrado'}), 404
        elif exists['Borrado'] is False:
            return fl.jsonify({'exists': 1, 'data': exists})
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500
