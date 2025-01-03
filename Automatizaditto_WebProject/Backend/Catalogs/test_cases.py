from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls

connection_string = fl.db_connection_func()


def insert_new_test_case():
    tc_name = fl.request.form['iTestCaseName']
    tc_azure_id = fl.request.form['iAzureId'] or None
    tc_product_id = fl.request.form['iProductId'] or None

    try:
        insert = connection_string.cursor()
        insert.execute(sql.insert_test_case, (tc_name, tc_azure_id, tc_product_id, fl.session['user_id'],))
        get_function_result = insert.fetchone()[0]

        print(get_function_result)

        if get_function_result.get('success') == 1:
            get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(5))
            connection_string.commit()
            insert.close()
            return fl.jsonify(get_function_result), 200
        else:
            return fl.jsonify(get_function_result), 404
    except Exception as e:
        connection_string.rollback()
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500


def update_test_case():
    u_tc_id = fl.request.form['uHiddenId']
    u_tc_name = fl.request.form['uTestCaseName']
    u_tc_azure_id = fl.request.form['uAzureId'] or None
    u_tc_product_id = fl.request.form['uProductId'] or None

    try:
        update = connection_string.cursor()
        update.execute(sql.update_test_case, (u_tc_id, u_tc_name, u_tc_azure_id, u_tc_product_id, fl.session['user_id']))
        get_function_result = update.fetchone()[0]

        print(get_function_result)

        if get_function_result.get('success') == 1:
            get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(5))
            connection_string.commit()
            update.close()
            return fl.jsonify(get_function_result), 200
        else:
            return fl.jsonify(get_function_result), 404
    except Exception as e:
        connection_string.rollback()
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500
