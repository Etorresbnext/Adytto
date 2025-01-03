from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls
import re

connection_string = fl.db_connection_func()


def insert_new_user():
    name = fl.request.form['name']
    lastname = fl.request.form['lastname']
    email = fl.request.form['email']
    password = fl.request.form['password']
    profile = fl.request.form['profile']

    try:
        if not name or not name.strip():
            return fl.jsonify({'message': 'Debe capturar un Nombre para el usuario'}), 404
        elif not lastname or not lastname.strip():
            return fl.jsonify({'message': 'Debe capturar el Apellido del usuario'}), 404
        elif not email or not email.strip():
            return fl.jsonify({'message': 'Debe capturar el Correo Electrónico del usuario'}), 404
        elif len(password) < 8:
            return fl.jsonify({'message': 'La contraseña debe contener al menos 8 caracteres'}), 404
        elif not any(char.isupper() for char in password):
            return fl.jsonify({'message': 'La contraseña debe contener al menos una letra mayúscula'}), 404
        elif not any(char.isdigit() for char in password):
            return fl.jsonify({'message': 'La contraseña debe contener al menos un número'}), 404
        elif not re.search(r'[\W_]', password):
            return fl.jsonify({'message': 'La contraseña adebe contener al menos un caracter especial'}), 404
        else:
            try:
                insert = connection_string.cursor(cursor_factory=fl.RealDictCursor)
                insert.execute(sql.insert_user, (fl.session['user_id'], name, lastname, email, password, profile,))
                connection_string.commit()
                insert.close()
                return fl.redirect(fl.url_for('render_page', page_name=urls(0)))
            except Exception as e:
                return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos', 'error': str(e)}), 500


def update_user():
    update_user_id = fl.request.form['updateID_hidden']
    update_user_name = fl.request.form['updateUserName']
    update_user_lastname = fl.request.form['updateUserLastName']
    update_user_email = fl.request.form['updateUserEmail']
    update_user_profile = fl.request.form['updateUserProfile']

    try:
        update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        update.execute(sql.update_user, (
            update_user_id, update_user_name, update_user_lastname, update_user_email, update_user_profile,
            fl.session['user_id'],))
        connection_string.commit()
        update.close()
        print(f"Actualizado por: {fl.session['user_id']}")  #Depuración
        return fl.redirect(fl.url_for('render_page', page_name=urls(0)))
    except Exception as e:
        return fl.jsonify({'message': 'Error en la Base de datos', 'error:': str(e)}), 500
