# Tomás Amaya y David Gaitán
from estilos import C_OK
from tkinter import messagebox

def ejecutar(entry1, entry2, lbl_resultado):
    try:
        v1 = entry1.get().strip()
        v2 = entry2.get().strip()
        if not v1 or not v2:
            messagebox.showwarning("Campos vacíos", "Ingrese ambos números.")
            return
        resultado = float(v1) * float(v2)
        texto = int(resultado) if resultado == int(resultado) else round(resultado, 6)
        lbl_resultado.config(text=f"Resultado: {texto}", fg=C_OK)
    except ValueError:
        messagebox.showerror("Error", "Ingrese únicamente valores numéricos.")
