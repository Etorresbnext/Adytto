from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls

connection_string = fl.db_connection_func()


def login():
    email = fl.request.form['user_email']
    password = fl.request.form['user_password']

    try:
        select = connection_string.cursor()
        select.execute(sql.user_access, (email,))
        user_auth = select.fetchone()
        if user_auth:
            if fl.bcrypt.checkpw(password.encode('utf-8'), user_auth[2].encode('utf-8')):
                fl.session['user_id'] = user_auth[0]

                select.execute(sql.get_user_permissions, (fl.session['user_id'],))
                select_permissions = select.fetchall()
                user_permissions = [i[0] for i in select_permissions]
                fl.session['permissions'] = user_permissions
                select.close()
                return fl.jsonify({'redirect_url': fl.url_for('render_page', page_name=urls(1))})
                #return fl.redirect(fl.url_for('render_page', page_name=urls(1)))
            else:
                return fl.jsonify({'message': 'Correo electrónico o contraseña incorrectos. Inténtelo nuevamente.'}), 404
        else:
            return fl.jsonify({'message': 'Correo electrónico o contraseña incorrectos. Inténtelo nuevamente.'}), 404

    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos', 'error:': str(e)}), 500


def logout():
    [fl.session.pop(i, None) for i in ('user_id', 'permissions', 'errors')]
    fl.flash('Has cerrado tu sesión correctamente')
    return fl.redirect(fl.url_for('login_template'))
