"""Tests de user_repository.py (mock Database)."""
import pytest
from unittest.mock import patch, MagicMock
from mysql.connector import IntegrityError
from user_repository import UserRepository, ConexionError


@pytest.fixture
def mock_db():
    with patch("user_repository.Database") as MockDB:
        mock_db_instance = MockDB.return_value
        yield mock_db_instance


def test_registrar_usuario_true_si_insert_ok(mock_db):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.is_connected.return_value = True
    mock_db.conectar.return_value = mock_conn

    repo = UserRepository()
    ok = repo.registrar_usuario("Ana", "123", "300", "a@b.com", "ana", "clave")

    assert ok is True
    mock_cursor.execute.assert_called_once()
    sql = mock_cursor.execute.call_args.args[0]
    assert "INSERT INTO usuarios" in sql


def test_registrar_usuario_lanza_integrityerror_si_duplicado(mock_db):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.is_connected.return_value = True
    mock_db.conectar.return_value = mock_conn
    mock_cursor.execute.side_effect = IntegrityError(1062, "Duplicate entry")

    repo = UserRepository()
    with pytest.raises(IntegrityError):
        repo.registrar_usuario("Ana", "123", "300", "a@b.com", "ana", "clave")


def test_registrar_usuario_false_si_error_generico(mock_db):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.is_connected.return_value = True
    mock_db.conectar.return_value = mock_conn
    mock_cursor.execute.side_effect = Exception("random error")

    repo = UserRepository()
    ok = repo.registrar_usuario("Ana", "123", "300", "a@b.com", "ana", "clave")
    assert ok is False


def test_registrar_usuario_lanza_conexionerror_si_sin_conexion(mock_db):
    mock_db.conectar.return_value = None
    repo = UserRepository()
    with pytest.raises(ConexionError):
        repo.registrar_usuario("Ana", "123", "300", "a@b.com", "ana", "clave")


def test_validar_usuario_devuelve_dict_si_match(mock_db):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.is_connected.return_value = True
    mock_db.conectar.return_value = mock_conn
    mock_cursor.fetchone.return_value = {
        "id": 1, "nombre": "Ana", "usuario": "ana",
        "cedula": "123", "celular": "300", "correo": "a@b.com"
    }

    repo = UserRepository()
    user = repo.validar_usuario("ana", "1234")

    assert user is not None
    assert user["nombre"] == "Ana"


def test_validar_usuario_none_si_no_match(mock_db):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.is_connected.return_value = True
    mock_db.conectar.return_value = mock_conn
    mock_cursor.fetchone.return_value = None

    repo = UserRepository()
    user = repo.validar_usuario("ana", "wrong")
    assert user is None


def test_validar_usuario_lanza_conexionerror_si_sin_conexion(mock_db):
    mock_db.conectar.return_value = None
    repo = UserRepository()
    with pytest.raises(ConexionError):
        repo.validar_usuario("ana", "1234")