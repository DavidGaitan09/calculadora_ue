# Tomás Amaya y David Gaitán
import tkinter as tk

from estilos import (C_FONDO, C_PANEL, C_BORDE, C_ACENTO, C_TEXTO,
                      C_SUBTEXTO, C_BTN, C_BTN_ALT, C_BTN_HOV,
                      C_MARCA_ROJO, pantalla_completa, hacer_firma)
import suma, resta, multiplicacion, division
from operacion_window import abrir_operacion


class HomeWindow:
    """HomeActivity: saludo al usuario, botón 'Cerrar sesión' y las
    4 opciones de la calculadora (Sumar, Restar, Multiplicar, Dividir),
    igual que en el tablero."""

    def __init__(self, login_window, datos_usuario):
        self.login_window = login_window
        self.datos_usuario = datos_usuario

        self.ventana = tk.Toplevel(login_window.ventana)
        self.ventana.title("Inicio")
        pantalla_completa(self.ventana)
        self.ventana.configure(bg=C_FONDO)
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_sesion)

        self.crear_componentes()

    def crear_componentes(self):
        tk.Frame(self.ventana, bg=C_ACENTO, height=4).pack(fill="x")

        # ── Barra superior: saludo + cerrar sesión ──────────────
        barra = tk.Frame(self.ventana, bg=C_FONDO)
        barra.pack(fill="x", padx=40, pady=(20, 0))

        nombre = self.datos_usuario.get("nombre", "")
        tk.Label(barra, text=f"Hola, {nombre}", font=("Segoe UI", 16, "bold"),
                 bg=C_FONDO, fg=C_TEXTO).pack(side="left")

        tk.Button(barra, text="Cerrar sesión", font=("Segoe UI", 11, "bold"),
                  command=self.cerrar_sesion, bg=C_MARCA_ROJO, fg=C_TEXTO,
                  relief="flat", bd=0, activebackground="#a80029",
                  activeforeground=C_TEXTO, cursor="hand2",
                  padx=16, pady=6).pack(side="right")

        tk.Label(self.ventana, text="¿Qué quieres hacer?",
                 font=("Segoe UI", 13), bg=C_FONDO, fg=C_SUBTEXTO
                 ).pack(pady=(30, 10))

        # ── Grid 2x2 con las 4 operaciones ──────────────────────
        wrapper = tk.Frame(self.ventana, bg=C_FONDO)
        wrapper.pack(expand=True, fill="both")
        wrapper.columnconfigure(0, weight=1)
        wrapper.columnconfigure(1, weight=0)
        wrapper.columnconfigure(2, weight=1)
        wrapper.rowconfigure(0, weight=1)

        grid_ops = tk.Frame(wrapper, bg=C_FONDO)
        grid_ops.grid(row=0, column=1)

        operaciones = [
            ("Sumar",       suma,           C_BTN),
            ("Restar",      resta,          C_BTN_ALT),
            ("Multiplicar", multiplicacion, C_BTN),
            ("Dividir",     division,       C_BTN_ALT),
        ]

        for i, (nombre_op, modulo, color) in enumerate(operaciones):
            fila, col = divmod(i, 2)
            tk.Button(grid_ops, text=nombre_op, font=("Segoe UI", 13, "bold"),
                      command=lambda n=nombre_op, m=modulo, c=color: self.abrir_operacion(n, m, c),
                      bg=color, fg=C_TEXTO, relief="flat", bd=0,
                      activebackground=C_BTN_HOV, activeforeground=C_TEXTO,
                      cursor="hand2", width=18
                      ).grid(row=fila, column=col, padx=14, pady=14, ipady=26)

        hacer_firma(self.ventana)

    def abrir_operacion(self, nombre_op, modulo, color):
        abrir_operacion_ventana = abrir_operacion(
            self.ventana, nombre_op, "Operaciones básicas", modulo, color)
        return abrir_operacion_ventana

    def cerrar_sesion(self):
        self.ventana.destroy()
        self.login_window.limpiar_campos()
        self.login_window.ventana.deiconify()
