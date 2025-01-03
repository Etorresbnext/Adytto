from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls


connection_string = fl.db_connection_func()


def load_page(page_name):
    user_session_id = fl.session.get('user_id')
    user_permissions = fl.session.get('permissions')

    if user_session_id:
        select = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        select.execute(sql.get_url_permission, (page_name,))
        url_permission = select.fetchone()
        select.close()

        if url_permission and url_permission['name'] in fl.session['permissions']:
            return fl.render_template(f'{page_name}.html', user_permissions=user_permissions)
        else:
            return fl.redirect(fl.url_for('render_page', page_name=urls(3)))
    else:
        return fl.redirect(fl.url_for('login_template'))
