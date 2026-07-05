"""Tests de la logica de division (incluye guard division por cero)."""
import pytest
import division


def test_div_enteros(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("20"), fake_entry("4"), fake_label()
    division.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: 5"


def test_div_resultado_decimal(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("10"), fake_entry("4"), fake_label()
    division.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: 2.5"


def test_div_por_cero_muestra_error(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("5"), fake_entry("0"), fake_label()
    division.ejecutar(e1, e2, lbl)
    assert lbl.text is None


def test_div_campo_vacio(fake_entry, fake_label):
    e1, e2, lbl = fake_entry(""), fake_entry("5"), fake_label()
    division.ejecutar(e1, e2, lbl)
    assert lbl.text is None


def test_div_no_numerico(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("x"), fake_entry("5"), fake_label()
    division.ejecutar(e1, e2, lbl)
    assert lbl.text is None