from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls

connection_string = fl.db_connection_func()


def insert_new_hard_drive():
    validity_errors = {}

    hard_drive_brand = fl.request.form['hardDriveBrand']
    if not hard_drive_brand or not hard_drive_brand.strip():
        validity_errors['nullBrand'] = 'Seleccione una marca para el Disco Duro.'

    hard_drive_type = fl.request.form['hardDriveType']
    if not hard_drive_type or not hard_drive_type.strip():
        validity_errors['nullType'] = 'Seleccione el tipo de Disco Duro.'

    hard_drive_storage = fl.request.form['hardDriveStorage']
    storage_unit = fl.request.form['storageUnits']

    if (not hard_drive_storage or not hard_drive_storage.strip()) or (not storage_unit or not storage_unit.strip()):
        validity_errors['nullStorage'] = 'Asegúrese de capturar la capacidad de almacenamiento del Disco Duro'

    if validity_errors:
        return fl.jsonify(validity_errors), 404

    try:
        insert = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        insert.execute(sql.insert_hard_drive, (hard_drive_brand, hard_drive_type, hard_drive_storage, storage_unit, fl.session['user_id'],))
        connection_string.commit()
        insert.close()
        return fl.jsonify({'redirect_url': fl.url_for('render_page', page_name=urls(11))})
    except Exception as e:
        print(e)
        connection_string.rollback()
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500


def update_hard_drive():
    update_hard_drive_id = fl.request.form['updateID_hidden']
    update_hard_drive_type = fl.request.form['updateHardDriveType']
    update_hard_drive_storage = fl.request.form['updateHardDriveStorage']

    try:
        if not update_hard_drive_storage or not update_hard_drive_storage.strip():
            return fl.jsonify({'messgae': 'Debe capturar la capacidad de almacenamiento del Disco Duro'}), 404
        else:
            try:
                update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
                update.execute(sql.update_hard_drive, (update_hard_drive_id, update_hard_drive_type, update_hard_drive_storage, fl.session['user_id'],))
                connection_string.commit()
                update.close()
                return fl.redirect(fl.url_for('render_page', page_name=urls(11)))
            except Exception as e:
                return fl.jsonify({'message': 'Error en la base de datos. Update no se realiza', 'error': str(e)}), 500
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos', 'error': str(e)}), 500
