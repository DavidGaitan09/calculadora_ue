import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "sistema_login"
        self.port = 3306

    def conectar(self):
        try:
            conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            return conexion
        except Error as error:
            print(f"Error de conexión: {error}")
            return None

    def inicializar(self):
        """
        Crea la tabla 'usuarios' si no existe todavía, con todos los
        campos que se piden en el formulario de Registro (Nombre,
        Cedula, Celular, Correo) más Usuario y Clave para el Login.
        Llamar una sola vez al arrancar la aplicación.
        """
        conexion = self.conectar()
        if conexion is None:
            return False
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    cedula VARCHAR(30) NOT NULL,
                    celular VARCHAR(30) NOT NULL,
                    correo VARCHAR(100) NOT NULL,
                    usuario VARCHAR(50) NOT NULL UNIQUE,
                    clave VARCHAR(100) NOT NULL
                )
            """)
            conexion.commit()
            return True
        except Exception as error:
            print(f"Error al inicializar la base de datos: {error}")
            return False
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
