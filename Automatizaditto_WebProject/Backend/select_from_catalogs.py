import base64

from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.select_functions import select_function as sf

connection_string = fl.db_connection_func()


def select_from_catalogs(catalog):
    try:
        select = connection_string.cursor(cursor_factory=fl.RealDictCursor)

        queries = {
            'products': sql.select_products,
            'users': sql.users,
            'profile_name': sql.profile_name,
            'test-cases': sql.select_test_cases,
            'objects': sql.select_objects,
            'object-types': sql.select_object_types,
            'environment_types': sql.select_environment_type,
            'urls': sql.select_paths,
            'protocols': sql.select_protocol,
            'runners': sql.select_runners,
            'hardware-configurations': sql.select_hard_conf,
            'software-configurations': sql.select_soft_conf,
            'processors': sql.select_processors,
            'processor_brands': sql.processor_brands,
            'processor-frequencies': sql.select_processor_frequencies,
            'processor-architectures': sql.select_processor_architectures,
            'hard-drives': sql.select_hard_drives,
            'hard-drives_brands': sql.hard_drives_brands,
            'hard-drives_types': sql.hard_drives_types,
            'hard-drives_storage': sql.hard_drives_storage,
            'rams': sql.select_rams,
            'operative-systems': sql.select_operative_system,
            'storage_units': sql.select_storage_units,
            'frequency_units': sql.select_frequency_units,
            'os_families': sql.select_family,
            'os_architectures': sql.select_architecture,
            'runners-status': sql.select_runners_status
        }

        if catalog not in queries:
            return fl.jsonify({'error': 'Información no valida'}), 400

        if catalog == 'profile_name':
            select.execute(queries[catalog], (fl.session['user_id'],))
            catalog_result = select.fetchone()
        elif catalog == 'runners-status':
            select.execute(queries[catalog])
            catalog_result = select.fetchall()

            result = []
            for image in catalog_result:
                if image['connected_led'] is not None:
                    converted_image = base64.b64encode(image['connected_led']).decode('utf-8')
                    result.append({
                        'id': image['id'],
                        'name': image['name'],
                        'ip': image['ip'],
                        'connected_led': converted_image,
                        'last_ping': image['last_ping']
                    })
                else:
                    result.append({
                        'id': image['id'],
                        'name': image['name'],
                        'ip': image['ip'],
                        'connected_led': None,
                        'last_ping': image['last_ping']
                    })

            catalog_result = result

        else:
            select.execute(queries[catalog])
            catalog_result = select.fetchall()
        select.close()
        return fl.jsonify(catalog_result)
    except Exception as e:
        print(f"Error al consultar información {catalog}: {e}")
        return fl.jsonify({'error': f'Error al consultar información {catalog}'})
