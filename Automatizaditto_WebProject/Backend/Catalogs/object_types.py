from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls

connection_string = fl.db_connection_func()


def insert_new_object_type():
    object_type_name = fl.request.form['iObjTypeName']

    try:
        insert = connection_string.cursor()
        insert.execute(sql.insert_object_type, (object_type_name, fl.session['user_id'],))
        get_function_result = insert.fetchone()[0]

        print(get_function_result)

        if get_function_result.get('success') == 1:
            get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(7))
            connection_string.commit()
            insert.close()
            return fl.jsonify(get_function_result), 200
        else:
            return fl.jsonify(get_function_result), 404
    except Exception as e:
        print(e)
        connection_string.rollback()
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500


def update_object_type():
    update_object_type_id = fl.request.form['updateID_hidden']
    update_object_type_name = fl.request.form['updateObjectTypeName']

    try:
        if not update_object_type_name or not update_object_type_name.strip():
            return fl.jsonify({'message': 'Debe capturar un nombre para el Tipo de Objeto'}), 404
        else:
            try:
                update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
                update.execute(sql.update_object_type,
                               (update_object_type_id, update_object_type_name, fl.session['user_id']))
                connection_string.commit()
                update.close()
                return fl.redirect(fl.url_for('render_page', page_name=urls(7)))
            except Exception as e:
                return fl.jsonify({'message': 'Error en la base de datos. UPDATE no se realiza', 'error': str(e)}), 500
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos', 'error': str(e)}), 500
