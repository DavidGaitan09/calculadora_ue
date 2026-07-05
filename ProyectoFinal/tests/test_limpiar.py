"""Tests de limpiar.py."""
import pytest
import limpiar


def test_limpiar_borra_campos_y_reset_label(fake_entry, fake_label):
    e1 = fake_entry("123")
    e2 = fake_entry("456")
    lbl = fake_label()
    lbl.text = "Resultado: 999"
    lbl.fg = "#ff0000"

    limpiar.ejecutar(e1, e2, lbl)

    assert e1._value == ""
    assert e2._value == ""
    assert lbl.text == "Resultado: ?"
    # El codigo original NO resetea fg, solo el texto