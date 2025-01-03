from Automatizaditto_WebProject.Backend import flask_libraries as fl
from Automatizaditto_WebProject.Backend import sql_scripts as sql
from Automatizaditto_WebProject.Backend.urls import urls

connection_string = fl.db_connection_func()


def insert_new_processor():
    validity_errors = {}

    processor_name = fl.request.form['processorName']
    print(processor_name)
    if not processor_name or not processor_name.strip():
        validity_errors['nullName'] = 'Asegúrese de capturar un nombre para el Procesador.'

    processor_brand = fl.request.form['processorBrand']
    print(processor_brand)
    if not processor_brand or not processor_brand.strip():
        validity_errors['nullBrand'] = 'Seleccione la marca del Procesador.'

    processor_model = fl.request.form['processorModel']
    print(processor_model)
    if not processor_model or not processor_model.strip():
        validity_errors['nullModel'] = 'Asegúrese de capturar el modelo del Procesador.'

    processor_freq = fl.request.form['processorFreq']
    print(processor_freq)
    freq_unit = fl.request.form['freqUnits']
    print(freq_unit)

    if (not processor_freq or not processor_freq.strip()) or (not freq_unit or not freq_unit.strip()):
        validity_errors['nullFreq'] = 'Asegúrese de capturar la frecuencia del Procesador.'

    processor_arch = fl.request.form['processorArch']
    print(processor_arch)
    if not processor_arch or not processor_arch.strip():
        validity_errors['nullArch'] = 'Seleccione la arquitectura del procesador.'

    if validity_errors:
        return fl.jsonify(validity_errors), 404

    frequency = processor_freq + ' ' + freq_unit

    try:
        insert = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        insert.execute(sql.insert_processor,
                       (processor_name, processor_brand, processor_model, frequency, processor_arch,
                        fl.session['user_id'],))
        connection_string.commit()
        insert.close()
        return fl.jsonify({'redirect_url': fl.url_for('render_page', page_name=urls(10))})
    except Exception as e:
        return fl.jsonify({'message': 'Error en la base de datos. Insert no se realiza', 'error': str(e)}), 500


def update_processor():

    update_errors = {}

    update_processor_id = fl.request.form['updateID_hidden']

    update_processor_name = fl.request.form['updateProcessorName']
    if not update_processor_name or not update_processor_name.strip():
        update_errors['nullName'] = 'Asegúrese de capturar el nombre actualizado del Procesador.'

    update_processor_brand = fl.request.form['updateProcessorBrand']

    update_processor_model = fl.request.form['updateProcessorModel']
    if not update_processor_model or not update_processor_model.strip():
        update_errors['nullModel'] = 'Asegúrese de capturar el modelo actualizado del Procesador.'

    update_processor_freq = fl.request.form['updateProcessorFreq']
    if not update_processor_freq or not update_processor_freq.strip():
        update_errors['nullFreq'] = 'Asegúrese de capturar la frecuencia actualizada del Procesador.'

    update_processor_units = fl.request.form['updateFreqUnits']
    update_processors_arch = fl.request.form['updateProcessorArch']

    full_frequency = update_processor_freq + ' ' + update_processor_units

    if update_errors:
        return fl.jsonify(update_errors), 404

    try:
        update = connection_string.cursor(cursor_factory=fl.RealDictCursor)
        update.execute(sql.update_processor, (
            update_processor_id, update_processor_name, update_processor_brand, update_processor_model,
            full_frequency, update_processors_arch, fl.session['user_id'],))
        connection_string.commit()
        update.close()
        return fl.jsonify({'redirect_url': fl.url_for('render_page', page_name=urls(10))})
    except Exception as e:
        print(e)
        return fl.jsonify({'message': 'Error en la base de datos. Update no se realiza', 'error': str(e)}), 500
