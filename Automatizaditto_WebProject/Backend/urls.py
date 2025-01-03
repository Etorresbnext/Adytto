from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql

connection_string = fl.db_connection_func()


def urls(url_id):
    try:
        select = connection_string.cursor()
        select.execute(sql.get_urls_names)
        result = select.fetchall()
        url_name = [i[0] for i in result]

    except Exception as e:
        return fl.jsonify({'message': 'Error en la Base de datos', 'error:': str(e)}), 500
    return url_name[url_id]
