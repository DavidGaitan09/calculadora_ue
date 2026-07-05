"""Tests de la logica de resta."""
import pytest
import resta


def test_resta_enteros(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("10"), fake_entry("3"), fake_label()
    resta.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: 7"


def test_resta_resultado_negativo(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("3"), fake_entry("10"), fake_label()
    resta.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: -7"


def test_resta_decimales_colapsa(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("5.5"), fake_entry("0.5"), fake_label()
    resta.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: 5"


def test_resta_decimales_no_enteros(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("5.25"), fake_entry("2"), fake_label()
    resta.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: 3.25"


def test_resta_campo_vacio(fake_entry, fake_label):
    e1, e2, lbl = fake_entry(""), fake_entry("5"), fake_label()
    resta.ejecutar(e1, e2, lbl)
    assert lbl.text is None


def test_resta_no_numerico(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("x"), fake_entry("5"), fake_label()
    resta.ejecutar(e1, e2, lbl)
    assert lbl.text is None


def test_resta_cero_a_cero(fake_entry, fake_label):
    e1, e2, lbl = fake_entry("0"), fake_entry("0"), fake_label()
    resta.ejecutar(e1, e2, lbl)
    assert lbl.text == "Resultado: 0"