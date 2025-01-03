from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql

connection_string = fl.db_connection_func()


def profile_picture():
    if not fl.session['user_id']:
        return fl.jsonify({'error': 'Usuario no autenticado'}), 401

    try:
        select = connection_string.cursor()
        select.execute(sql.profile_picture, (fl.session['user_id'],))
        image_data = select.fetchone()
        print(f"Imagen obtenida: {image_data[0]}")
        print(f"Mime Type obtenido: {image_data[1]}")
        if image_data:
            return fl.Response(image_data[0], mimetype=image_data[1])
        else:
            return fl.jsonify({'error': 'Imagen no encontrada'}), 404
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos', 'error:': str(e)}), 500
    finally:
        select.close()