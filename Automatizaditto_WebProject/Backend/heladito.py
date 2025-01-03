from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend.render_pages import load_page as lp
from Automatizaditto_WebProject.Backend.auth import login, logout
from Automatizaditto_WebProject.Backend.profile_picture import profile_picture as pp
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.delete_from_catalogs import delete_from_catalogs as delete
from Automatizaditto_WebProject.Backend.select_from_catalogs import select_from_catalogs as select
from Automatizaditto_WebProject.Backend.urls import urls
from Automatizaditto_WebProject.Backend.Catalogs import object_types, objects, test_cases, users, products_urls, \
    runners, processors, hard_drives, rams, operative_systems, hardware_configurations, software_configurations, \
    products
import re
from Automatizaditto_WebProject.Backend.select_functions import select_function as sf

heladito = fl.Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')
heladito.config['SECRET_KEY'] = 'h3l4dit0_*k3y'
heladito.config['SESSION_COOKIE_NAME'] = 'session'

connection_string = fl.db_connection_func()


#Ruta para renderizar la página de Inicio de Sesión
@heladito.route('/')
def login_template():
    return fl.render_template('login.html')


#Ruta para autenticación de usuario e iniciar sesión
@heladito.route('/login', methods=['POST'])
def auth_login():
    return login()  #Función definida en auth.py


#Ruta para cerrar sesión
@heladito.route('/logout', methods=['POST'])
def auth_logout():
    return logout()  #Función definida en auth.py


#Ruta dinámica para renderizar páginas
@heladito.route('/<page_name>')
def render_page(page_name):
    return lp(page_name)  #Función definida en render_pages.py


#Ruta para consultar información de los catálogos
@heladito.route('/select/<catalog>', methods=['GET'])
def select_data(catalog):
    return select(catalog)  #Función definida en select_from_catalogs.py


@heladito.route('/get_user_image')
def get_image():
    return pp()

# ------------------------------------------------------------------------------------------------------------------- #
# BORRAR REGISTROS DE CATÁLOGOS
@heladito.route('/delete/<record>', methods=['POST'])
def delete_record(record):
    return delete(record)  #Función definida en delete_from_catalogs


# ------------------------------------------------------------------------------------------------------------------- #
# INSERTAR UN NUEVO PRODUCTO
@heladito.route('/insert/product', methods=['POST'])
def insert_new_product():
    return products.insert_new_product()


# ACTUALIZAR UN PRODUCTO
@heladito.route('/update/product', methods=['POST'])
def update_product():
    return products.update_product()
# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# INSERTAR UN NUEVO CASO DE PRUEBA
@heladito.route('/insert/test-case', methods=['POST'])
def insert_new_test_case():
    return test_cases.insert_new_test_case()


# ACTUALIZAR UN CASO DE PRUEBA
@heladito.route('/update/test-case', methods=['POST'])
def update_test_cases():
    return test_cases.update_test_case()
# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
# INSERTAR UN NUEVO TIPO DE OBJETO
@heladito.route('/insert/object-type', methods=['POST'])
def insert_new_object_type():
    return object_types.insert_new_object_type()


# ACTUALIZAR UN TIPO DE OBJETO
@heladito.route('/update/object-type', methods=['POST'])
def update_object_type():
    return object_types.update_object_type()
# ------------------------------------------------------------------------------------------------------------------- #


@heladito.route('/insert_object', methods=['POST'])
def insert_new_object():
    return objects.insert_new_object()


@heladito.route('/update_object', methods=['POST'])
def update_object():
    return objects.update_object()


@heladito.route('/insert_user', methods=['POST'])
def insert_new_user():
    return users.insert_new_user()


@heladito.route('/update_user', methods=['POST'])
def update_users():
    return users.update_user()


@heladito.route('/insert_url', methods=['POST'])
def insert_new_url():
    return products_urls.insert_new_url()


@heladito.route('/update_url', methods=['POST'])
def update_url():
    return products_urls.update_url()


# ------------------------------------------------------------------------------------------------------------------- #
# Rutas para Insertar y Actualizar Catálogo Runners
@heladito.route('/insert_runner', methods=['POST'])
def insert_new_runner():
    return runners.insert_new_runner()


@heladito.route('/update_runner', methods=['POST'])
def update_runner():
    return runners.update_runner()


@heladito.route('/verify_hard_conf', methods=['POST'])
def verify_hardware_configuration():
    return runners.verify_hardware_configuration()


@heladito.route('/verify_soft_conf', methods=['POST'])
def verify_software_configuration():
    return runners.verify_software_configuration()


# ------------------------------------------------------------------------------------------------------------------- #


#Rutas para Insertar y Actualizar Procesadores
@heladito.route('/insert_processor', methods=['POST'])
def insert_new_processor():
    return processors.insert_new_processor()


@heladito.route('/update_processor', methods=['POST'])
def update_processor():
    return processors.update_processor()


#Rutas para Insertar y Actualizar Discos Duros
@heladito.route('/insert_hard-drive', methods=['POST'])
def insert_new_hard_drive():
    return hard_drives.insert_new_hard_drive()


@heladito.route('/update_hard-drive', methods=['POST'])
def update_hard_drive():
    return hard_drives.update_hard_drive()


# ------------------------------------------------------------------------------------------------------------------- #
#Rutas para Insertar y Actualizar Memorias RAM
@heladito.route('/insert_ram', methods=['GET', 'POST'])
def insert_new_ram():
    return rams.insert_new_ram()


@heladito.route('/update_ram', methods=['POST'])
def update_ram():
    return rams.update_ram()


# ------------------------------------------------------------------------------------------------------------------- #
#Rutas para Insertar y Actualizar Sistemas Operativos
@heladito.route('/insert_operative_system', methods=['POST'])
def insert_new_operative_system():
    return operative_systems.insert_new_operative_system()


@heladito.route('/update_operative_system', methods=['POST'])
def update_operative_system():
    return operative_systems.update_operative_system()


# ------------------------------------------------------------------------------------------------------------------- #
#Rutas para Insertar y Actualizar Configuraciones de Hardware
@heladito.route('/insert_hardware_configuration', methods=['POST'])
def insert_new_hardware_configuration():
    return hardware_configurations.insert_new_hardware_configuration()


@heladito.route('/update_hardware_configuration', methods=['POST'])
def update_hardware_configuration():
    return hardware_configurations.update_hardware_configuration()


# ------------------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------------------- #
#Rutas para Insertar y Actualizar Configuraciones de Software
@heladito.route('/insert_software_configuration', methods=['POST'])
def insert_new_software_configuration():
    return software_configurations.insert_new_software_configuration()


@heladito.route('/update_software_configuration', methods=['POST'])
def update_software_configuration():
    return software_configurations.update_software_configuration()


@heladito.route('/update_user_full_name', methods=['POST'])
def update_user_full_name():
    update_name = fl.request.form['getUserName']
    update_lastname = fl.request.form['getUserLastName']

    if 'profileImage' in fl.request.files:
        file = fl.request.files['profileImage']
        if file.filename:
            print(file.filename)
            new_profile_picture = file.read()
            mime_type = file.content_type
            is_new_picture = True
        else:
            print('No se seleccionó ningún archivo')
            new_profile_picture = None
            mime_type = None
            is_new_picture = False
    else:
        print("No hay archivos en request.files")
        new_profile_picture = None
        mime_type = None
        is_new_picture = False

    try:
        update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        update.execute(sql.update_user_profile, (
            fl.session['user_id'], update_name, update_lastname, new_profile_picture, mime_type, is_new_picture,
            fl.session['user_id'],))
        connection_string.commit()
        update.close()
        return fl.redirect(fl.url_for('render_page', page_name=urls(2)))
    except Exception as e:
        return fl.jsonify({'message': 'Error en la Base de datos', 'error:': str(e)}), 500


@heladito.route('/update_user_password', methods=['POST'])
def update_user_password():
    update_pass_id = fl.request.form['updateUserPassID']
    update_pass_new = fl.request.form['updateNewPass']
    update_pass_new_confirm = fl.request.form['updateNewPassConfirm']
    print(f"Nueva contraseña recibida: {update_pass_new}")

    try:
        if len(update_pass_new) < 8:
            return fl.jsonify({'message': 'La contraseña debe contener al menos 8 caracteres'}), 404
        elif not any(char.isupper() for char in update_pass_new):
            return fl.jsonify({'message': 'La contraseña debe contener al menos una letra mayúscula'}), 404
        elif not any(char.isdigit() for char in update_pass_new):
            return fl.jsonify({'message': 'La contraseña debe contener al menos un número'}), 404
        elif not re.search(r'[\W_]', update_pass_new):
            return fl.jsonify({'message': 'La contraseña adebe contener al menos un caracter especial'}), 404
        else:
            try:
                update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
                update.execute(sql.update_user_pass,
                               (update_pass_new, update_pass_new_confirm, update_pass_id, fl.session['user_id'],))
                connection_string.commit()
                update.close()
                return fl.redirect(fl.url_for('render_page', page_name=urls(0)))
            except Exception as e:
                return fl.jsonify(
                    {'message': 'Error en la Base de datos. Nueva contraseña no coincide', 'error:': str(e)}), 500
    except Exception as e:
        return fl.jsonify({'message': 'Error en la Base de datos', 'error:': str(e)}), 500


@heladito.route('/set_new_password', methods=['POST'])
def set_new_password():
    update_pass_current = fl.request.form['updateCurrentPass']
    update_pass_new = fl.request.form['updateNewPass']
    update_pass_new_confirm = fl.request.form['updateNewPassConfirm']
    print(f"Nueva contraseña recibida: {update_pass_new}")

    select = connection_string.cursor(cursor_factory=fl.RealDictCursor)
    select.execute(sql.select_user_pass, (fl.session['user_id'],))
    current_password = select.fetchone()

    if fl.bcrypt.checkpw(update_pass_current.encode('utf-8'), current_password['user_password'].encode('utf-8')):
        try:
            if len(update_pass_new) < 8:
                return fl.jsonify({'message': 'La contraseña debe contener al menos 8 caracteres'}), 404
            elif not any(char.isupper() for char in update_pass_new):
                return fl.jsonify({'message': 'La contraseña debe contener al menos una letra mayúscula'}), 404
            elif not any(char.isdigit() for char in update_pass_new):
                return fl.jsonify({'message': 'La contraseña debe contener al menos un número'}), 404
            elif not re.search(r'[\W_]', update_pass_new):
                return fl.jsonify({'message': 'La contraseña adebe contener al menos un caracter especial'}), 404
            else:
                try:
                    update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
                    update.execute(sql.update_user_pass, (
                        update_pass_new, update_pass_new_confirm, fl.session['user_id'], fl.session['user_id'],))
                    connection_string.commit()
                    update.close()
                    return fl.jsonify({'message': 'Contraseña actualizada exitosamente',
                                       'redirect_url': fl.url_for('render_page', page_name=urls(2))}), 200
                except Exception as e:
                    return fl.jsonify(
                        {'message': 'Error en la Base de datos. Nueva contraseña no coincide', 'error:': str(e)}), 500
        except Exception as e:
            return fl.jsonify({'message': 'Error en la Base de datos', 'error:': str(e)}), 500
    else:
        return fl.jsonify({'message': 'Contraseña actual incorrecta. Inténtelo nuevamente'}), 404


if __name__ == '__main__':
    heladito.run(host="0.0.0.0", port=5000, debug=True)
