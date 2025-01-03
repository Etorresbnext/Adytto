from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend.urls import urls
from Automatizaditto_WebProject.Backend import sql_scripts as sql

connection_string = fl.db_connection_func()


def insert_new_product():
    product_name = fl.request.form['productName']
    product_desc = fl.request.form['productDesc']

    try:
        insert = connection_string.cursor()
        insert.execute(sql.insert_product, (product_name, product_desc, fl.session['user_id'],))
        get_function_result = insert.fetchone()[0]

        print(get_function_result)

        if get_function_result.get('success') == 1:
            get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(4))
            connection_string.commit()
            insert.close()
            return fl.jsonify(get_function_result), 200
        else:
            return fl.jsonify(get_function_result), 404
    except Exception as e:
        print(e)
        connection_string.rollback()
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500


def update_product():
    u_product_id = fl.request.form['uHiddenId']
    u_product_name = fl.request.form['uProductName']
    u_product_desc = fl.request.form['uProductDesc']

    try:
        update = connection_string.cursor()
        update.execute(sql.update_product, (u_product_id, u_product_name, u_product_desc, fl.session['user_id'],))
        get_function_result = update.fetchone()[0]

        print(get_function_result)

        if get_function_result.get('success') == 1:
            get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(4))
            connection_string.commit()
            update.close()
            return fl.jsonify(get_function_result), 200
        else:
            return fl.jsonify(get_function_result), 404
    except Exception as e:
        connection_string.rollback()
        print(e)
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500
