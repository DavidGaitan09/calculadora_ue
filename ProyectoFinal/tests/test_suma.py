"""Tests de la logica de suma (sin Tkinter real: usamos fixtures FakeEntry/FakeLabel)."""
import pytest
import suma


def test_suma_enteros_muestra_entero(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("2"), fake_entry("3"), fake_label()
    suma.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: 5"
    assert lbl.fg == "#22c55e"


def test_suma_decimales_colapsa_a_entero(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("2.5"), fake_entry("2.5"), fake_label()
    suma.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: 5"


def test_suma_decimales_no_enteros_redondea_6(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("1.5"), fake_entry("2"), fake_label()
    suma.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: 3.5"


def test_suma_negativos(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("-4"), fake_entry("2"), fake_label()
    suma.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: -2"


def test_suma_campo_vacio_muestra_warning(fake_entry, fake_label):
    """El warning se silencia por fixture no_messagebox; solo verificamos que no crashea."""
    e1, e2, lbl = fake_entry(""), fake_entry("5"), fake_label()
    suma.ejecutar(e1, e2, lbl)
    # Si hay warning, lbl.text queda None
    assert lbl.text is None


def test_suma_no_numerico_muestra_error(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("abc"), fake_entry("5"), fake_label()
    suma.ejecutar(e1, e2, lbl)
    assert lbl.text is None


def test_suma_strips_espacios(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("  7  "), fake_entry("  3  "), fake_label()
    suma.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: 10"