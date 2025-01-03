from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls

connection_string = fl.db_connection_func()


def insert_new_ram():
    ram_capacity = fl.request.form['ramCapacity']
    ram_capacity_unit = fl.request.form['ramCapacityUnits']
    ram_frequency = fl.request.form['ramFrequency']
    ram_frequency_unit = fl.request.form['ramFrequencyUnits']
    ram_technology = fl.request.form['ramTech']
    ram_full_capacity = ram_capacity + ' ' + ram_capacity_unit
    ram_full_frequency = ram_frequency + ' ' + ram_frequency_unit

    try:
        insert = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        insert.execute(sql.insert_ram, (ram_full_capacity, ram_full_frequency, ram_technology, fl.session['user_id'],))
        connection_string.commit()
        insert.close()
        return fl.redirect(fl.url_for('render_page', page_name=urls(13)))
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500


def update_ram():
    update_ram_id = fl.request.form['updateID_hidden']
    update_ram_capacity = fl.request.form['updateRamCapacity']
    update_ram_capacity_unit = fl.request.form['updateRamCapacityUnits']
    update_ram_frequency = fl.request.form['updateRamFrequency']
    update_ram_frequency_unit = fl.request.form['updateRamFrequencyUnits']
    update_ram_technology = fl.request.form['updateRamTech']
    update_ram_full_capacity = update_ram_capacity + ' ' + update_ram_capacity_unit
    update_ram_full_frequency = update_ram_frequency + ' ' + update_ram_frequency_unit

    try:
        update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        update.execute(sql.update_ram, (update_ram_id, update_ram_full_capacity, update_ram_full_frequency, update_ram_technology, fl.session['user_id'],))
        connection_string.commit()
        update.close()
        return fl.redirect(fl.url_for('render_page', page_name=urls(13)))
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500
