# Tomás Amaya y David Gaitán
import tkinter as tk
from tkinter import messagebox

from estilos import (C_FONDO, C_ACENTO, C_TEXTO, C_SUBTEXTO, C_BTN,
                      ventana_centrada, hacer_firma, make_scrollable_center,
                      hacer_campo, hacer_boton)
from user_repository import UserRepository


class RegisterWindow:
    """RegisterActivity: flecha para volver al Login (arriba a la
    izquierda, igual que en el tablero), campos Nombre / Cedula /
    Celular / Correo / Usuario / Clave, y el botón 'Registrar'."""

    def __init__(self, login_ventana):
        self.login_ventana = login_ventana
        self.repository = UserRepository()

        self.ventana = tk.Toplevel(login_ventana)
        self.ventana.title("Registro")
        ventana_centrada(self.ventana, ancho=560, alto=760)
        self.ventana.configure(bg=C_FONDO)
        self.ventana.grab_set()

        self.crear_componentes()

    def crear_componentes(self):
        tk.Frame(self.ventana, bg=C_ACENTO, height=4).pack(fill="x")

        # ── Barra superior con flecha de regreso ────────────────
        barra = tk.Frame(self.ventana, bg=C_FONDO)
        barra.pack(fill="x", padx=24, pady=(14, 0))
        tk.Button(barra, text="←", font=("Segoe UI", 16, "bold"),
                  command=self.volver_al_login, bg=C_FONDO, fg=C_ACENTO,
                  relief="flat", bd=0, activebackground=C_FONDO,
                  activeforeground=C_ACENTO, cursor="hand2").pack(side="left")

        tk.Label(self.ventana, text="Registro", font=("Segoe UI", 20, "bold"),
                 bg=C_FONDO, fg=C_ACENTO).pack(pady=(6, 2))
        tk.Label(self.ventana, text="Crea tu cuenta para acceder a la calculadora",
                 font=("Segoe UI", 10), bg=C_FONDO, fg=C_SUBTEXTO).pack(pady=(0, 4))

        c = make_scrollable_center(self.ventana, width=420)

        self.txt_nombre = hacer_campo(c, 0, "Nombre:", ancho=38)
        self.txt_cedula = hacer_campo(c, 1, "Cedula:", ancho=38)
        self.txt_celular = hacer_campo(c, 2, "Celular:", ancho=38)
        self.txt_correo = hacer_campo(c, 3, "Correo:", ancho=38)
        self.txt_usuario = hacer_campo(c, 4, "Usuario:", ancho=38)
        self.txt_clave = hacer_campo(c, 5, "Clave:", ancho=38, oculto=True)

        hacer_boton(c, "Registrar", self.registrar, color=C_BTN, ancho=30,
                    row=12, column=0, pady=(22, 20), ipady=12)

        hacer_firma(self.ventana)

    def registrar(self):
        nombre = self.txt_nombre.get().strip()
        cedula = self.txt_cedula.get().strip()
        celular = self.txt_celular.get().strip()
        correo = self.txt_correo.get().strip()
        usuario = self.txt_usuario.get().strip()
        clave = self.txt_clave.get().strip()

        if not all([nombre, cedula, celular, correo, usuario, clave]):
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios")
            return

        registrado = self.repository.registrar_usuario(
            nombre, cedula, celular, correo, usuario, clave)

        if registrado:
            messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente")
            self.volver_al_login()
        else:
            messagebox.showerror("Error", "No se pudo registrar el usuario")

    def volver_al_login(self):
        self.ventana.destroy()
        self.login_ventana.deiconify()
