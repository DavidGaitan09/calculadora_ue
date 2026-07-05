# Tomas Amaya y David Gaitan
"""Ventana genérica para una operación (Sumar, Restar, Multiplicar o
Dividir), reutilizando la lógica original de suma.py / resta.py /
multiplicacion.py / division.py."""
import tkinter as tk
from estilos import (C_FONDO, C_PANEL, C_BORDE, C_ACENTO, C_TEXTO,
                     C_SUBTEXTO, F_LABEL, F_ENTRY, F_RES, F_BTN,
                     base_ventana, hacer_header, hacer_firma, make_center)
import limpiar


def abrir_operacion(root, titulo, subtitulo, modulo_operacion, color_btn):
    v = base_ventana(root, titulo)
    hacer_header(v, titulo, subtitulo)
    c = make_center(v)

    tk.Label(c, text="Número 1", font=F_LABEL, bg=C_FONDO,
             fg=C_SUBTEXTO, anchor="w", width=48).grid(
        row=0, column=0, sticky="w", pady=(20, 4))
    e1 = tk.Entry(c, font=F_ENTRY, bg=C_PANEL, fg=C_TEXTO,
                  insertbackground=C_ACENTO, relief="flat",
                  highlightthickness=1, highlightbackground=C_BORDE,
                  highlightcolor=C_ACENTO, width=48)
    e1.grid(row=1, column=0, sticky="ew", ipady=10, pady=(0, 4))

    tk.Label(c, text="Número 2", font=F_LABEL, bg=C_FONDO,
             fg=C_SUBTEXTO, anchor="w", width=48).grid(
        row=2, column=0, sticky="w", pady=(16, 4))
    e2 = tk.Entry(c, font=F_ENTRY, bg=C_PANEL, fg=C_TEXTO,
                  insertbackground=C_ACENTO, relief="flat",
                  highlightthickness=1, highlightbackground=C_BORDE,
                  highlightcolor=C_ACENTO, width=48)
    e2.grid(row=3, column=0, sticky="ew", ipady=10, pady=(0, 4))

    lbl_res = tk.Label(c, text="Resultado: ?", font=F_RES,
                      bg=C_FONDO, fg=C_ACENTO)
    lbl_res.grid(row=4, column=0, pady=22)

    tk.Frame(c, bg=C_BORDE, height=1).grid(row=5, column=0, sticky="ew")

    frame_btns = tk.Frame(c, bg=C_FONDO)
    frame_btns.grid(row=6, column=0, pady=16)

    tk.Button(frame_btns, text=titulo, font=F_BTN,
              command=lambda: modulo_operacion.ejecutar(e1, e2, lbl_res),
              bg=color_btn, fg=C_TEXTO, relief="flat", bd=0,
              activebackground=C_ACENTO, cursor="hand2",
              width=16).grid(row=0, column=0, padx=8, pady=6, ipady=12)

    tk.Button(frame_btns, text="Limpiar", font=F_BTN,
              command=lambda: limpiar.ejecutar(e1, e2, lbl_res),
              bg="#475569", fg=C_TEXTO, relief="flat", bd=0,
              activebackground="#64748b", cursor="hand2",
              width=16).grid(row=0, column=1, padx=8, pady=6, ipady=12)

    hacer_firma(v)
    return v