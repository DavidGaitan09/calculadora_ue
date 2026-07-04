# Tomás Amaya y David Gaitán
"""
Estilos compartidos por toda la aplicación (Login, Registro, Home y
las calculadoras). Se mantiene la misma paleta oscura que ya usaban
las calculadoras para que TODAS las pantallas se vean exactamente igual.
"""
import os
import tkinter as tk

# ── Paleta base (idéntica a la de las calculadoras) ────────────────
C_FONDO    = "#0f172a"
C_PANEL    = "#1e293b"
C_BORDE    = "#334155"
C_ACENTO   = "#38bdf8"
C_TEXTO    = "#f1f5f9"
C_SUBTEXTO = "#94a3b8"
C_BTN      = "#1d4ed8"
C_BTN_HOV  = "#2563eb"
C_ERROR    = "#ef4444"
C_OK       = "#22c55e"
C_BTN_ALT  = "#312e81"

# ── Colores de marca Uniempresarial (tomados del logo) ─────────────
C_MARCA_ROJO = "#de0034"
C_MARCA_AZUL = "#0d1f86"

# ── Tipografías ─────────────────────────────────────────────────
F_TITULO = ("Segoe UI", 15, "bold")
F_LABEL  = ("Segoe UI", 11)
F_ENTRY  = ("Segoe UI", 13)
F_BTN    = ("Segoe UI", 12, "bold")
F_RES    = ("Segoe UI", 15, "bold")
F_FIRMA  = ("Segoe UI", 9)

FIRMA_TEXTO = "Realizado por Tomás Amaya y David Gaitán"

ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")


def pantalla_completa(v):
    """Deja la ventana/toplevel en pantalla completa, igual que las calculadoras."""
    try:
        v.state("zoomed")
    except Exception:
        sw = v.winfo_screenwidth()
        sh = v.winfo_screenheight()
        v.geometry(f"{sw}x{sh}+0+0")
    v.resizable(True, True)


def ventana_centrada(v, ancho=560, alto=760):
    """Deja la ventana/toplevel con un tamaño fijo (NO pantalla completa),
    centrada en la pantalla del usuario. Se puede seguir redimensionando
    a mano si el contenido lo necesita."""
    v.update_idletasks()
    sw = v.winfo_screenwidth()
    sh = v.winfo_screenheight()

    # Si la pantalla es más pequeña que el tamaño pedido, se ajusta
    # dejando un margen, para que nunca quede más grande que la pantalla.
    ancho = min(ancho, sw - 40)
    alto = min(alto, sh - 60)

    x = (sw - ancho) // 2
    y = (sh - alto) // 2
    v.geometry(f"{ancho}x{alto}+{x}+{y}")
    v.minsize(min(420, ancho), min(500, alto))
    v.resizable(True, True)


def base_ventana(root, titulo):
    """Toplevel en pantalla completa con el mismo estilo oscuro, usado
    por las ventanas de operaciones (Sumar, Restar, Multiplicar, Dividir)."""
    v = tk.Toplevel(root)
    v.title(titulo)
    pantalla_completa(v)
    v.configure(bg=C_FONDO)
    v.grab_set()
    return v


def hacer_firma(v):
    """Pie de página igual en Login, Registro y Home."""
    tk.Frame(v, bg=C_BORDE, height=1).pack(fill="x", padx=40, pady=(10, 0), side="bottom")
    tk.Label(v, text=FIRMA_TEXTO, font=F_FIRMA, bg=C_FONDO,
              fg=C_SUBTEXTO).pack(side="bottom", pady=8)


def hacer_header(v, titulo, sub):
    f = tk.Frame(v, bg=C_PANEL)
    f.pack(fill="x", side="top")
    tk.Label(f, text=titulo, font=F_TITULO, bg=C_PANEL,
             fg=C_ACENTO, pady=14).pack()
    if sub:
        tk.Label(f, text=sub, font=("Segoe UI", 10), bg=C_PANEL,
                 fg=C_SUBTEXTO).pack(pady=(0, 10))
    tk.Frame(v, bg=C_ACENTO, height=2).pack(fill="x", side="top")


def make_center(v, width=460):
    """Frame centrado horizontalmente con ancho fijo para el contenido."""
    wrapper = tk.Frame(v, bg=C_FONDO)
    wrapper.pack(fill="both", expand=True)
    wrapper.columnconfigure(0, weight=1)
    wrapper.columnconfigure(1, weight=0)
    wrapper.columnconfigure(2, weight=1)
    wrapper.rowconfigure(0, weight=1)
    center = tk.Frame(wrapper, bg=C_FONDO, width=width)
    center.grid(row=0, column=1, sticky="ns", pady=30)
    center.columnconfigure(0, weight=1)
    return center


def make_scrollable_center(v, width=460):
    """Igual que make_center (frame centrado para meter campos), pero
    con una barra de scroll vertical que aparece sola si el contenido
    no cabe en la ventana. Así el botón final SIEMPRE es alcanzable,
    sin importar el tamaño de la ventana o de la pantalla."""
    contenedor = tk.Frame(v, bg=C_FONDO)
    contenedor.pack(fill="both", expand=True)

    canvas = tk.Canvas(contenedor, bg=C_FONDO, highlightthickness=0, bd=0)
    scrollbar = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)

    wrapper = tk.Frame(canvas, bg=C_FONDO)
    ventana_id = canvas.create_window((0, 0), window=wrapper, anchor="n")

    def _actualizar_scrollregion(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))
        # Solo se muestra la barra si el contenido de verdad no cabe
        if wrapper.winfo_reqheight() > canvas.winfo_height():
            scrollbar.pack(side="right", fill="y")
        else:
            scrollbar.pack_forget()

    def _ajustar_ancho(event):
        canvas.itemconfig(ventana_id, width=event.width)

    wrapper.bind("<Configure>", _actualizar_scrollregion)
    canvas.bind("<Configure>", _ajustar_ancho)

    def _rueda_raton(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _activar_rueda(event):
        canvas.bind_all("<MouseWheel>", _rueda_raton)

    def _desactivar_rueda(event):
        canvas.unbind_all("<MouseWheel>")

    canvas.bind("<Enter>", _activar_rueda)
    canvas.bind("<Leave>", _desactivar_rueda)

    center = tk.Frame(wrapper, bg=C_FONDO, width=width)
    center.pack(pady=30)
    center.columnconfigure(0, weight=1)
    return center


def hacer_campo(frame, fila_idx, etiqueta, ancho=42, oculto=False):
    tk.Label(frame, text=etiqueta, font=F_LABEL, bg=C_FONDO,
             fg=C_SUBTEXTO, anchor="w", width=ancho).grid(
        row=fila_idx * 2, column=0, sticky="w", padx=0, pady=(14, 3))
    e = tk.Entry(frame, font=F_ENTRY, bg=C_PANEL, fg=C_TEXTO,
                 insertbackground=C_ACENTO, relief="flat",
                 show="*" if oculto else "",
                 highlightthickness=1, highlightbackground=C_BORDE,
                 highlightcolor=C_ACENTO, width=ancho)
    e.grid(row=fila_idx * 2 + 1, column=0, sticky="ew", padx=0, pady=(0, 4), ipady=10)
    return e


def hacer_boton(parent, texto, cmd, color=None, ancho=20, **grid_kwargs):
    if color is None:
        color = C_BTN
    b = tk.Button(parent, text=texto, font=F_BTN, command=cmd,
                  bg=color, fg=C_TEXTO, relief="flat", bd=0,
                  activebackground=C_BTN_HOV, activeforeground=C_TEXTO,
                  cursor="hand2", width=ancho)
    b.grid(**grid_kwargs)
    return b


def leer(e, nombre):
    val = e.get().strip()
    if not val:
        raise ValueError(f"El campo '{nombre}' no puede estar vacío.")
    return float(val)


def cargar_logo(parent, size=150):
    """Carga el logo de Uniempresarial como PhotoImage (usa Pillow si está
    disponible para poder redimensionar; si no, la redimensiona igual con
    subsample para que nunca se muestre a tamaño completo)."""
    ruta = os.path.join(ASSETS_DIR, "logo.png")
    try:
        from PIL import Image, ImageTk
        img = Image.open(ruta).convert("RGBA")
        img = img.resize((size, size), Image.LANCZOS)
        foto = ImageTk.PhotoImage(img, master=parent)
    except Exception:
        foto = tk.PhotoImage(file=ruta, master=parent)
        ancho_actual = foto.width()
        if ancho_actual > size:
            factor = max(1, round(ancho_actual / size))
            foto = foto.subsample(factor, factor)
    return foto
