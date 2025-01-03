#Credenciales de Acceso para Iniciar Sesión
user_access = 'SELECT * FROM system.select_user_credentials(%s)'
get_user_permissions = 'SELECT * FROM system.select_user_permissions(%s)'
get_auth_error = ('SELECT JSONB_BUILD_OBJECT((SELECT key FROM system.input_errors WHERE id = 12), (SELECT value FROM ''system.input_errors WHERE id = 12))')

user_profile_code = '''SELECT up.code FROM system.users u LEFT JOIN system.user_profiles up ON up.uuid = 
u.user_profile_uuid WHERE u.id = %s'''  #Obtener el código del Perfil

users = 'SELECT * FROM system.select_users()'  #Usuarios Activos y No Borrados

insert_user = 'SELECT system.insert_new_user(%s, %s, %s, %s, %s, %s)'  #Insertar usuarios
delete_user = 'SELECT system.delete_user(%s, %s)'  #Borrar usuarios
update_user = 'SELECT system.update_user(%s, %s, %s, %s, %s, %s)'

#Contraseña Usuario
select_user_pass = 'SELECT user_password FROM system.users WHERE id = %s'
update_user_pass = 'SELECT system.update_user_password(%s, %s, %s, %s)'

#Solo Nombre y Apellido Usuario
profile_name = 'SELECT name AS "Nombre", lastname AS "Apellido" FROM system.users WHERE id = %s'
profile_picture = '''SELECT u.profile_picture, mt.name FROM system.users u LEFT JOIN system.mime_types mt ON mt.uuid 
        = u.mime_type_uuid WHERE u.id = %s'''
update_user_full_name = 'UPDATE system.users SET name = %s, lastname = %s, updated_date = now(), updated_by = (SELECT uuid FROM system.users WHERE id = %s) WHERE id = %s'

#Nombre de Usuario e Imagen
update_user_profile = 'SELECT system.update_user_profile(%s, %s, %s, %s, %s, %s, %s)'

#Código de Perfil de Usuario


#Información de Perfil
profile_data = 'SELECT * FROM system.select_profile_data(%s)'

#Páginas
get_urls_names = 'SELECT name FROM system.urls ORDER BY id'

#Permisos


#Permiso asociado a Página
get_url_permission = '''SELECT uper.name FROM system.urls urlp LEFT JOIN system.user_permissions uper ON uper.uuid = urlp.user_permission_uuid WHERE urlp.name = %s'''


# --------------------------------------- ESQUEMA test_management --------------------------------------- #


# Casos de Prueba (test_cases)
select_test_cases = 'SELECT * FROM test_management.select_test_cases()'
insert_test_case = 'SELECT test_management.insert_new_test_case(%s, %s, %s, %s)'
update_test_case = 'SELECT test_management.update_test_case(%s, %s, %s, %s, %s)'
delete_test_case = 'SELECT test_management.delete_test_case(%s, %s)'


# ------------------------------------------------------------------------------------------------------ #


# --------------------------------------- ESQUEMA web_automation --------------------------------------- #


# Objetos (objects)
select_objects = 'SELECT * FROM web_automation.select_objects()'
insert_objects = 'SELECT test.insert_web_objects(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
delete_objects = 'SELECT test.delete_object(%s, %s)'
update_objects = 'SELECT test.update_web_object(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'


# Tipos de Objeto (object_types)
select_object_types = 'SELECT * FROM web_automation.select_object_types()'
insert_object_type = 'SELECT web_automation.insert_new_object_type(%s, %s)'
update_object_type = 'SELECT test.update_object_type(%s, %s, %s)'
delete_object_type = 'SELECT test.delete_object_type(%s, %s)'


# Productos (products)
select_products = 'SELECT * FROM web_automation.select_products()'
insert_product = 'SELECT web_automation.insert_new_product(%s, %s, %s)'
update_product = 'SELECT web_automation.update_product(%s, %s, %s, %s)'
delete_product = 'SELECT web_automation.delete_product(%s, %s)'


# Rutas (paths)
select_paths = 'SELECT * FROM web_automation.select_paths()'
insert_url = 'SELECT test.insert_new_url(%s, %s, %s, %s, %s, %s)'
delete_url = 'SELECT test.delete_url(%s, %s)'
update_url = 'SELECT test.update_url(%s, %s, %s, %s, %s, %s, %s)'




#Ambientes
select_environment_type = 'SELECT * FROM test.select_environment_types()'

#Protocolos
select_protocol = 'SELECT * FROM test.select_web_protocol()'



#Runners
select_runners = '''SELECT
                        r.id,
                        r.name, 
                        r.description, 
                        r.ip, 
                        hc.id AS "id_hc",
                        hc.name AS "name_hc", 
                        sc.id AS "id_sc",
                        sc.name AS "name_sc"
                    FROM runners_configuration.runners r
                        LEFT JOIN runners_configuration.hardware_configurations hc ON hc.uuid = r.hardware_configuration_uuid
                        LEFT JOIN runners_configuration.software_configurations sc ON sc.uuid = r.software_configuration_uuid
                    WHERE r.active = true AND r.deleted = false
                    ORDER BY r.id'''

insert_runner = 'SELECT runners_configuration.insert_new_runner(%s, %s, %s, %s, %s, %s)'
delete_runner = 'SELECT runners_configuration.delete_runner(%s, %s)'
update_runner = 'SELECT runners_configuration.update_runner(%s, %s, %s, %s, %s, %s, %s)'

#Hardware Configurations
select_hard_conf = 'SELECT * FROM runners_configuration.select_hardware_configurations()'
insert_hard_conf = 'SELECT runners_configuration.insert_new_hardware_configuration(%s, %s, %s, %s, %s, %s)'
delete_hard_conf = 'SELECT runners_configuration.delete_hardware_configuration(%s, %s)'
update_hard_conf = 'SELECT runners_configuration.update_hardware_configuration(%s, %s, %s, %s, %s, %s, %s)'

#Software Configurations
select_soft_conf = 'SELECT * FROM runners_configuration.select_software_configurations()'
insert_soft_conf = 'SELECT runners_configuration.insert_new_software_configuration(%s, %s, %s, %s)'
delete_soft_conf = 'SELECT runners_configuration.delete_software_configuration(%s, %s)'
update_soft_conf = 'SELECT runners_configuration.update_software_configuration(%s, %s, %s, %s, %s)'

#Procesadores
select_processors = 'SELECT * FROM runners_configuration.select_processors()'
select_dblink_processors = 'SELECT * FROM dblink.select_processors(1)'
insert_processor = 'SELECT runners_configuration.insert_new_processor(%s, %s, %s, %s, %s, %s)'
delete_processor = 'SELECT runners_configuration.delete_processor(%s, %s)'
update_processor = 'SELECT runners_configuration.update_processor(%s, %s, %s, %s, %s, %s, %s)'
processor_brands = 'SELECT * FROM runners_configuration.processor_brands()'
select_processor_frequencies = 'SELECT * FROM runners_configuration.select_processor_frequencies()'
select_processor_architectures = 'SELECT * FROM runners_configuration.select_processor_architectures()'

#Discos Duros
select_hard_drives = 'SELECT * FROM runners_configuration.select_hard_drives()'
insert_hard_drive = 'SELECT runners_configuration.insert_new_hard_drive(%s, %s, %s, %s, %s)'
delete_hard_drive = 'SELECT runners_configuration.delete_hard_drive(%s, %s)'
update_hard_drive = 'SELECT runners_configuration.update_hard_drive(%s, %s, %s, %s)'
hard_drives_types = 'SELECT * FROM runners_configuration.select_hard_drive_types()'
hard_drives_storage = 'SELECT * FROM runners_configuration.select_hard_drive_storages()'
hard_drives_brands = 'SELECT * FROM runners_configuration.hard_drive_brands()'

#RAMS
select_rams = 'SELECT * FROM runners_configuration.select_rams()'
insert_ram = 'SELECT runners_configuration.insert_new_ram(%s, %s, %s, %s)'
delete_ram = 'SELECT runners_configuration.delete_ram(%s, %s)'
update_ram = 'SELECT runners_configuration.update_ram(%s, %s, %s, %s, %s)'

#Sistemas Operativos
select_operative_system = 'SELECT * FROM runners_configuration.select_operative_systems()'
insert_operative_system = 'SELECT runners_configuration.insert_new_operative_system(%s, %s, %s, %s, %s, %s)'
delete_operative_system = 'SELECT runners_configuration.delete_operative_system(%s, %s)'
update_operative_system = 'SELECT runners_configuration.update_operative_system(%s, %s, %s, %s, %s, %s, %s)'

#Unidades
select_storage_units = '''SELECT * FROM (VALUES('MB'),('GB'),('TB')) AS units("Units")'''
select_frequency_units = '''SELECT * FROM (VALUES('MHz'),('GHz')) AS units("Frequency")'''

#Sistemas Operativos
select_family = '''SELECT * FROM (VALUES('Microsoft Windows'), ('Linux'), ('Debian'), ('Android')) AS os("Operative_Systems")'''
select_architecture = '''SELECT * FROM (VALUES('x86'), ('x64'), ('ARM'), ('ARM64')) AS os("Architecture")'''

#Verificar Existencia de Configuración de Hardware y Software
select_verify_hard_conf = 'SELECT * FROM runners_configuration.verify_hardware_configuration(%s, %s, %s)'
select_verify_soft_conf = 'SELECT * FROM runners_configuration.verify_software_configuration(%s)'

select_runners_status = 'SELECT id, name, ip, connected_led, last_ping FROM runners_configuration.runners WHERE active = true AND deleted = false ORDER BY id'
