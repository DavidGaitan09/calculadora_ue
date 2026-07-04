# Tomás Amaya y David Gaitán
import tkinter as tk

def ejecutar(entry1, entry2, lbl_resultado):
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    lbl_resultado.config(text="Resultado: —")
