import psycopg2

# Función para establecer conexión con la Base de Datos
def db_connection_func():
    connection_string = psycopg2.connect(
        database="AdyttoDEV",  # Nombre de la Base de Datos
        user="postgres",            # Usuario con el que se accede a la Base de Datos
        host='localhost',           # Host/Equipo en donde se encuentra alojada la Base de Datos
        password="postgres",        # Contraseña con la que se accede a la Base de Datos
        port=5447                   # Puerto del Servidor Postgres en donde se encuentra alojada la Base de Datos
    )
    return connection_string