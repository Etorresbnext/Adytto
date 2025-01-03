from Automatizaditto_WebProject.Backend import flask_libraries as fl


def select_function(row_index, colum_index, catalog_id):
    connection_string = fl.db_connection_func()

    try:
        select = connection_string.cursor()
        select.execute('SELECT * FROM system.select_function(%s)', (catalog_id,))
        catalog_functions = select.fetchall()
        select.close()
        connection_string.close()
        return catalog_functions[row_index][colum_index]
    except Exception as e:
        connection_string.rollback()
        return fl.jsonify({'error': f'Error al consultar información {e}'})
