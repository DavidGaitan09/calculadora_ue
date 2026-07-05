# Tomas Amaya y David Gaitan
import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Carga las variables del archivo .env si existe; si no, usa valores por defecto.
load_dotenv()


class Database:
    """Conexion a MySQL y creacion automatica del esquema `sistema_login`.

    Las credenciales se leen de variables de entorno (ver .env.example):
      MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_DATABASE
    """

    def __init__(self):
        self.host = os.getenv("MYSQL_HOST", "localhost")
        self.user = os.getenv("MYSQL_USER", "root")
        self.password = os.getenv("MYSQL_PASSWORD", "")
        self.database = os.getenv("MYSQL_DATABASE", "sistema_login")
        self.port = int(os.getenv("MYSQL_PORT", "3306"))

    def conectar(self, usar_base=True):
        """Abre una conexion MySQL.

        `usar_base=False` conecta sin seleccionar una base de datos: se usa
        para poder ejecutar `CREATE DATABASE IF NOT EXISTS` antes de que la
        BD exista. Retorna None si la conexion falla.
        """
        try:
            kwargs = dict(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
            )
            if usar_base:
                kwargs["database"] = self.database
            return mysql.connector.connect(**kwargs)
        except Error as error:
            print(f"Error de conexion: {error}")
            return None

    def asegurar_base_datos(self):
        """Crea la base de datos 'sistema_login' si no existe todavia.

        Se conecta SIN especificar database para poder ejecutar el
        CREATE DATABASE. Llamar una sola vez al arrancar, antes de
        inicializar().
        """
        conexion = self.conectar(usar_base=False)
        if conexion is None:
            return False
        cursor = None
        try:
            cursor = conexion.cursor()
            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS `{self.database}` "
                f"DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
            )
            conexion.commit()
            return True
        except Exception as error:
            print(f"Error al crear la base de datos: {error}")
            return False
        finally:
            if cursor is not None:
                cursor.close()
            if conexion.is_connected():
                conexion.close()

    def inicializar(self):
        """Crea la tabla 'usuarios' si no existe todavia, con todos los
        campos que se piden en el formulario de Registro (Nombre,
        Cedula, Celular, Correo) mas Usuario y Clave para el Login.

        Requiere que la base de datos ya exista (ver asegurar_base_datos).
        """
        conexion = self.conectar()
        if conexion is None:
            return False
        cursor = None
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
            if cursor is not None:
                cursor.close()
            if conexion.is_connected():
                conexion.close()