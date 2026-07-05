"""Tests de la logica de multiplicacion."""
import pytest
import multiplicacion


def test_mult_enteros(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("6"), fake_entry("7"), fake_label()
    multiplicacion.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: 42"


def test_mult_por_cero(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("999"), fake_entry("0"), fake_label()
    multiplicacion.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: 0"


def test_mult_decimales(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("2.5"), fake_entry("4"), fake_label()
    multiplicacion.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: 10"


def test_mult_negativos(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("-3"), fake_entry("4"), fake_label()
    multiplicacion.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: -12"


def test_mult_campo_vacio(fake_entry, fake_label):
    e1, e2, lbl = fake_entry(""), fake_entry("5"), fake_label()
    multiplicacion.ejecutar(e1, e2, lbl)
    assert lbl.text is None


def test_mult_no_numerico(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("x"), fake_entry("5"), fake_label()
    multiplicacion.ejecutar(e1, e2, lbl)
    assert lbl.text is None