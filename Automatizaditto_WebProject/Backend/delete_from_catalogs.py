from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls

connection_string = fl.db_connection_func()


def delete_from_catalogs(record):
    delete_record_id = fl.request.form['dHiddenId']
    try:
        delete = connection_string.cursor()

        queries = {
            'delete_product': sql.delete_product,
            'delete_user': sql.delete_user,
            'delete_test-case': sql.delete_test_case,
            'delete_object-type': sql.delete_object_type,
            'delete_object': sql.delete_objects,
            'delete_url': sql.delete_url,
            'delete_runner': sql.delete_runner,
            'delete_processor': sql.delete_processor,
            'delete_hard-drive': sql.delete_hard_drive,
            'delete_ram': sql.delete_ram,
            'delete_os': sql.delete_operative_system,
            'delete_hard_conf': sql.delete_hard_conf,
            'delete_soft_conf': sql.delete_soft_conf
        }

        if record not in queries:
            return fl.jsonify({'error': 'Información no válida'}), 400

        delete.execute(queries[record], (delete_record_id, fl.session['user_id'],))
        connection_string.commit()
        '''get_function_result = delete.fetchone()[0]
        print(get_function_result)'''

        #if get_function_result.get('success') == 1:
        if record == 'delete_product':
            #get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(4))
            return fl.redirect(fl.url_for('render_page', page_name=urls(4)))
        elif record == 'delete_user':
            #get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(0))
            return fl.redirect(fl.url_for('render_page', page_name=urls(0)))
        elif record == 'delete_test-case':
            #get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(5))
            return fl.redirect(fl.url_for('render_page', page_name=urls(5)))
        elif record == 'delete_object':
            #get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(6))
            return fl.redirect(fl.url_for('render_page', page_name=urls(6)))
        elif record == 'delete_object-type':
            #get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(7))
            return fl.redirect(fl.url_for('render_page', page_name=urls(7)))
        elif record == 'delete_url':
            #get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(8))
            return fl.redirect(fl.url_for('render_page', page_name=urls(8)))
        elif record == 'delete_runner':
            #get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(9))
            return fl.redirect(fl.url_for('render_page', page_name=urls(9)))
        elif record == 'delete_processor':
            #get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(10))
            return fl.redirect(fl.url_for('render_page', page_name=urls(10)))
        elif record == 'delete_hard-drive':
            #get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(11))
            return fl.redirect(fl.url_for('render_page', page_name=urls(11)))
        elif record == 'delete_hard_conf':
            #get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(12))
            return fl.redirect(fl.url_for('render_page', page_name=urls(12)))
        elif record == 'delete_ram':
            #get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(13))
            return fl.redirect(fl.url_for('render_page', page_name=urls(13)))
        elif record == 'delete_os':
            #get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(14))
            return fl.redirect(fl.url_for('render_page', page_name=urls(14)))
        elif record == 'delete_soft_conf':
            #get_function_result['redirect_url'] = fl.url_for('render_page', page_name=urls(15))
            return fl.redirect(fl.url_for('render_page', page_name=urls(15)))
        #connection_string.commit()
        delete.close()
        #return fl.jsonify(get_function_result), 200
    except Exception as e:
        print(e)
        connection_string.rollback()
        return fl.jsonify({'message': 'Error en la Base de datos', 'error:': str(e)}), 500
