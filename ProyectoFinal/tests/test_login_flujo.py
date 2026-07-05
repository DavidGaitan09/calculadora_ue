"""Smoke tests del flujo de Login (con Tkinter mockeado).

Se skipean porque este entorno no tiene display Tkinter funcional.
"""
import pytest

# Skip todo el modulo: Tkinter no tiene display en este entorno
pytest.skip("Tkinter sin display funcional en este entorno", allow_module_level=True)

# Los tests se mantienen abajo por documentacion, pero no se ejecutan
from unittest.mock import patch, MagicMock
from user_repository import ConexionError

@patch("login_window.Database")
@patch("login_window.UserRepository")
def test_login_valido_abre_home(MockRepo, MockDB):
    from login_window import LoginWindow
    MockDB.return_value.asegurar_base_datos.return_value = True
    MockDB.return_value.inicializar.return_value = True
    mock_repo = MockRepo.return_value
    mock_repo.validar_usuario.return_value = {
        "id": 1, "nombre": "Ana", "usuario": "ana", "cedula": "", "celular": "", "correo": "",
    }
    app = LoginWindow()
    try:
        app.txt_usuario.insert(0, "ana")
        app.txt_clave.insert(0, "1234")
        with patch.object(app, "abrir_home") as mock_home:
            app.login()
            mock_home.assert_called_once()
            assert mock_home.call_args.args[0]["nombre"] == "Ana"
    finally:
        app.ventana.destroy()

@patch("login_window.Database")
@patch("login_window.UserRepository")
def test_login_invalido_muestra_error(MockRepo, MockDB):
    from login_window import LoginWindow
    MockDB.return_value.asegurar_base_datos.return_value = True
    MockDB.return_value.inicializar.return_value = True
    MockRepo.return_value.validar_usuario.return_value = None
    app = LoginWindow()
    try:
        app.txt_usuario.insert(0, "no")
        app.txt_clave.insert(0, "existo")
        with patch("tkinter.messagebox.showerror") as mock_err:
            with patch.object(app, "abrir_home") as mock_home:
                app.login()
                mock_err.assert_called_once()
                assert mock_err.call_args.args[0] == "Acceso denegado"
                mock_home.assert_not_called()
    finally:
        app.ventana.destroy()

@patch("login_window.Database")
@patch("login_window.UserRepository")
def test_login_campos_vacios_muestra_warning(MockRepo, MockDB):
    from login_window import LoginWindow
    MockDB.return_value.asegurar_base_datos.return_value = True
    MockDB.return_value.inicializar.return_value = True
    app = LoginWindow()
    try:
        with patch("tkinter.messagebox.showwarning") as mock_warn:
            with patch.object(app, "abrir_home") as mock_home:
                app.login()
                mock_warn.assert_called_once()
                mock_home.assert_not_called()
                MockRepo.return_value.validar_usuario.assert_not_called()
    finally:
        app.ventana.destroy()

@patch("login_window.Database")
@patch("login_window.UserRepository")
def test_login_sin_conexion_muestra_mensaje_distinto(MockRepo, MockDB):
    from login_window import LoginWindow
    MockDB.return_value.asegurar_base_datos.return_value = True
    MockDB.return_value.inicializar.return_value = True
    MockRepo.return_value.validar_usuario.side_effect = ConexionError("down")
    app = LoginWindow()
    try:
        app.txt_usuario.insert(0, "ana")
        app.txt_clave.insert(0, "1234")
        with patch("tkinter.messagebox.showerror") as mock_err:
            with patch.object(app, "abrir_home") as mock_home:
                app.login()
                mock_err.assert_called_once()
                assert mock_err.call_args.args[0] == "Sin conexi\u00f3n"
                mock_home.assert_not_called()
    finally:
        app.ventana.destroy()