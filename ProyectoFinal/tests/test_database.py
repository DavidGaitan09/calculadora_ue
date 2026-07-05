"""Tests de database.py (mock mysql.connector)."""
import pytest
from unittest.mock import patch, MagicMock
import database


@pytest.fixture
def mock_connector():
    with patch("database.mysql.connector.connect") as mock_connect:
        yield mock_connect


def test_asegurar_base_datos_crea_bd_si_no_existe(mock_connector):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.is_connected.return_value = True
    mock_connector.return_value = mock_conn

    db = database.Database()
    ok = db.asegurar_base_datos()

    assert ok is True
    mock_connector.assert_called_once()
    # Verifica que se conecto SIN database=
    args, kwargs = mock_connector.call_args
    assert "database" not in kwargs
    # Verifica SQL ejecutado
    mock_cursor.execute.assert_called()
    sql = mock_cursor.execute.call_args.args[0]
    assert "CREATE DATABASE IF NOT EXISTS" in sql
    assert "sistema_login" in sql


def test_inicializar_crea_tabla(mock_connector):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.is_connected.return_value = True
    mock_connector.return_value = mock_conn

    db = database.Database()
    ok = db.inicializar()

    assert ok is True
    mock_connector.assert_called_once()
    args, kwargs = mock_connector.call_args
    assert kwargs.get("database") == "sistema_login"
    sql = mock_cursor.execute.call_args.args[0]
    assert "CREATE TABLE IF NOT EXISTS usuarios" in sql


def test_inicializar_retorna_false_si_no_hay_conexion(mock_connector):
    mock_connector.return_value = None
    db = database.Database()
    ok = db.inicializar()
    assert ok is False


def test_conectar_retorna_none_en_error(mock_connector):
    import mysql.connector
    mock_connector.side_effect = mysql.connector.Error("fail")
    db = database.Database()
    conn = db.conectar()
    assert conn is None