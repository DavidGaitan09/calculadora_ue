"""Configuracion comun para los tests de ProyectoFinal."""
import os
import sys
import pytest

PROYECTO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROYECTO_DIR not in sys.path:
    sys.path.insert(0, PROYECTO_DIR)


class FakeEntry:
    """Mock minimo de tkinter.Entry: solo .get() y .delete()."""
    def __init__(self, value=""):
        self._value = value

    def get(self):
        return self._value

    def delete(self, *args):
        self._value = ""


class FakeLabel:
    """Mock minimo de tkinter.Label: solo .config(text=, fg=)."""
    def __init__(self):
        self.text = None
        self.fg = None

    def config(self, text=None, fg=None):
        if text is not None:
            self.text = text
        if fg is not None:
            self.fg = fg


@pytest.fixture
def fake_entry():
    return FakeEntry


@pytest.fixture
def fake_label():
    return FakeLabel


@pytest.fixture(autouse=True)
def no_messagebox(monkeypatch):
    """Silencia el messagebox de Tkinter para todos los tests."""
    monkeypatch.setattr("tkinter.messagebox.showwarning", lambda *a, **k: None)
    monkeypatch.setattr("tkinter.messagebox.showerror", lambda *a, **k: None)
    monkeypatch.setattr("tkinter.messagebox.showinfo", lambda *a, **k: None)