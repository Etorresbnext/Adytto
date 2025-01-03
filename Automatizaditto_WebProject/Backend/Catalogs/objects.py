from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls

connection_string = fl.db_connection_func()


def insert_new_object():
    object_name = fl.request.form['objectName']
    object_description = fl.request.form['objectDescription']
    object_id_g = fl.request.form['objectIdGrouper']
    object_name_g = fl.request.form['objectNameGrouper']
    object_class_g = fl.request.form['objectClassGrouper']
    object_xpath_g = fl.request.form['objectXpathGrouper']
    object_type = fl.request.form['objectType']
    object_product = fl.request.form['objectProduct']

    validity_errors = {}

    if not object_name or not object_name.strip():
        validity_errors['nullName'] = 'Asegúrese de capturar un nombre para el Objeto. Este campo es requerido.'

    if not object_type or not object_type.strip():
        validity_errors['nullType'] = 'Asegúrese de seleccionar un Tipo de Objeto. Este campo es requerido.'

    if not object_product or not object_product.strip():
        validity_errors['nullProduct'] = 'Asegúrese de seleccionar un Producto. Este campo es requerido.'

    if validity_errors:
        return fl.jsonify(validity_errors), 404

    try:
        insert = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        insert.execute(sql.insert_objects,
                       (object_name, object_description, object_id_g, object_name_g, object_class_g,
                        object_xpath_g, object_type, object_product, fl.session['user_id'],))
        connection_string.commit()
        insert.close()
        return fl.jsonify({'redirect_url': fl.url_for('render_page', page_name=urls(6))})
        #return fl.redirect(fl.url_for('render_page', page_name=urls(6)))
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500


def update_object():
    update_object_id = fl.request.form['updateID_hidden']
    update_object_name = fl.request.form['updateObjectName']
    update_object_description = fl.request.form['updateObjectDescription']
    update_object_id_g = fl.request.form['updateObjectIdGrouper']
    update_object_name_g = fl.request.form['updateObjectNameGrouper']
    update_object_class_g = fl.request.form['updateObjectClassGrouper']
    update_object_xpath_g = fl.request.form['updateObjectXpathGrouper']
    update_object_obj_type = fl.request.form['updateObjectType']
    update_object_product = fl.request.form['updateObjectProduct']

    try:
        if not update_object_name or not update_object_name.strip():
            return fl.jsonify({'message': 'Debe capturar un nombre para el Objeto'})
        else:
            try:
                update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
                update.execute(sql.update_objects,
                               (update_object_id,
                                update_object_name,
                                update_object_description,
                                update_object_id_g,
                                update_object_name_g,
                                update_object_class_g,
                                update_object_xpath_g,
                                update_object_obj_type,
                                update_object_product,
                                fl.session['user_id'],))
                connection_string.commit()
                update.close()
                return fl.redirect(fl.url_for('render_page', page_name=urls(6)))
            except Exception as e:
                return fl.jsonify({'message': 'Error en la base de datos. UPDATE no se realiza', 'error': str(e)}), 500
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos', 'error': str(e)}), 500
