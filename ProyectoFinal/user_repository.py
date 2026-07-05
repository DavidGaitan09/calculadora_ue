# Tomas Amaya y David Gaitan
from database import Database
from mysql.connector import IntegrityError


class ConexionError(Exception):
    """Se lanza cuando no se puede conectar a la base de datos."""


class UserRepository:
    def __init__(self):
        self.db = Database()

    def registrar_usuario(self, nombre, cedula, celular, correo, usuario, clave):
        """Inserta un usuario nuevo. Retorna True si todo fue bien.

        Lanza ConexionError si la conexion a MySQL falla.
        Lanza IntegrityError si el usuario ya existe (UNIQUE constraint).
        """
        conexion = self.db.conectar()
        if conexion is None:
            raise ConexionError("No se pudo conectar a la base de datos.")

        cursor = None
        try:
            cursor = conexion.cursor()
            sql = """
                INSERT INTO usuarios (nombre, cedula, celular, correo, usuario, clave)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (nombre, cedula, celular, correo, usuario, clave)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except IntegrityError:
            raise
        except Exception as error:
            print(f"Error al registrar usuario: {error}")
            return False
        finally:
            if cursor is not None:
                cursor.close()
            if conexion.is_connected():
                conexion.close()

    def validar_usuario(self, usuario, clave):
        """Devuelve el diccionario del usuario si las credenciales son
        correctas, o None si no lo son. Lanza ConexionError si no se
        puede conectar a MySQL.
        """
        conexion = self.db.conectar()
        if conexion is None:
            raise ConexionError("No se pudo conectar a la base de datos.")

        cursor = None
        try:
            cursor = conexion.cursor(dictionary=True)
            sql = """
                SELECT id, nombre, cedula, celular, correo, usuario
                FROM usuarios
                WHERE usuario = %s AND clave = %s
            """
            valores = (usuario, clave)
            cursor.execute(sql, valores)
            return cursor.fetchone()
        except Exception as error:
            print(f"Error al validar usuario: {error}")
            return None
        finally:
            if cursor is not None:
                cursor.close()
            if conexion.is_connected():
                conexion.close()