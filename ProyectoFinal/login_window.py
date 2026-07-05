# Tomas Amaya y David Gaitan
import tkinter as tk
from tkinter import messagebox

from estilos import (C_FONDO, C_PANEL, C_BORDE, C_ACENTO, C_TEXTO,
                     C_SUBTEXTO, C_BTN, C_BTN_ALT, C_BTN_HOV,
                     pantalla_completa, hacer_firma, make_center,
                     hacer_campo, hacer_boton, cargar_logo)
from user_repository import UserRepository, ConexionError
from database import Database


class LoginWindow:
    """LoginActivity: logo de Uniempresarial arriba, Usuario / Clave
    y los botones 'Registrarme' y 'Login', igual que en el tablero."""

    def __init__(self):
        self.repository = UserRepository()
        # Crea la BD (si no existe) y luego la tabla 'usuarios'.
        Database().asegurar_base_datos()
        Database().inicializar()

        self.ventana = tk.Tk()
        self.ventana.title("Login")
        pantalla_completa(self.ventana)
        self.ventana.configure(bg=C_FONDO)

        self.crear_componentes()

    def crear_componentes(self):
        tk.Frame(self.ventana, bg=C_ACENTO, height=4).pack(fill="x")

        c = make_center(self.ventana, width=420)

        # Logo Uniempresarial
        self._logo_img = cargar_logo(c, size=130)
        tk.Label(c, image=self._logo_img, bg=C_FONDO).grid(
            row=0, column=0, pady=(10, 4))
        tk.Label(c, text="Uniempresarial", font=("Segoe UI", 16, "bold"),
                 bg=C_FONDO, fg=C_ACENTO).grid(row=1, column=0, pady=(0, 20))

        # Usuario / Clave
        self.txt_usuario = hacer_campo(c, 1, "Usuario", ancho=38)
        self.txt_clave = hacer_campo(c, 2, "Clave", ancho=38, oculto=True)

        # Botones Registrarme / Login
        frame_btns = tk.Frame(c, bg=C_FONDO)
        frame_btns.grid(row=6, column=0, pady=(24, 10))

        hacer_boton(frame_btns, "Registrarme", self.abrir_registro,
                    color=C_BTN_ALT, ancho=16,
                    row=0, column=0, padx=8, ipady=12)
        hacer_boton(frame_btns, "Login", self.login,
                    color=C_BTN, ancho=16,
                    row=0, column=1, padx=8, ipady=12)

        hacer_firma(self.ventana)

    def login(self):
        usuario = self.txt_usuario.get().strip()
        clave = self.txt_clave.get().strip()

        if usuario == "" or clave == "":
            messagebox.showwarning("Campos vacíos", "Ingrese usuario y clave")
            return

        try:
            datos_usuario = self.repository.validar_usuario(usuario, clave)
        except ConexionError:
            messagebox.showerror(
                "Sin conexión",
                "No se pudo conectar a la base de datos. "
                "Verifique que MySQL esté corriendo y que el .env sea correcto."
            )
            return

        if datos_usuario:
            self.abrir_home(datos_usuario)
        else:
            messagebox.showerror("Acceso denegado", "Usuario o clave incorrectos")

    def abrir_registro(self):
        from register_window import RegisterWindow
        RegisterWindow(self.ventana)

    def abrir_home(self, datos_usuario):
        from home_window import HomeWindow
        self.ventana.withdraw()
        HomeWindow(self, datos_usuario)

    def limpiar_campos(self):
        self.txt_usuario.delete(0, tk.END)
        self.txt_clave.delete(0, tk.END)

    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    LoginWindow().ejecutar()