from database import Database


class UserRepository:
    def __init__(self):
        self.db = Database()

    def registrar_usuario(self, nombre, cedula, celular, correo, usuario, clave):
        conexion = self.db.conectar()

        if conexion is None:
            return False

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

        except Exception as error:
            print(f"Error al registrar usuario: {error}")
            return False

        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

    def validar_usuario(self, usuario, clave):
        """
        Devuelve el diccionario del usuario (nombre, cedula, celular,
        correo, usuario) si las credenciales son correctas, o None si
        no lo son. El HomeActivity usa el 'nombre' para el saludo.
        """
        conexion = self.db.conectar()

        if conexion is None:
            return None

        try:
            cursor = conexion.cursor(dictionary=True)
            sql = """
                SELECT id, nombre, cedula, celular, correo, usuario
                FROM usuarios
                WHERE usuario = %s AND clave = %s
            """
            valores = (usuario, clave)

            cursor.execute(sql, valores)
            resultado = cursor.fetchone()

            return resultado

        except Exception as error:
            print(f"Error al validar usuario: {error}")
            return None

        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
