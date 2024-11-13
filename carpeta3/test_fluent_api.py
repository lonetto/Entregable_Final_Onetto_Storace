import pytest
from unittest import mock
from conexion_bd import (conectar_db, crear_tablas, insertar_usuarios,
                         insertar_empleados, insertar_clientes, insertar_pedidos, insertar_ventas)

def test_conectar_db():
    with mock.patch('psycopg2.connect') as mock_connect:
        conexion_mock = mock.Mock()
        cursor_mock = mock.Mock()
        mock_connect.return_value = conexion_mock
        conexion_mock.cursor.return_value = cursor_mock

        conexion, cursor = conectar_db()
        assert conexion == conexion_mock
        assert cursor == cursor_mock

    
    with mock.patch('psycopg2.connect', side_effect=ConnectionError("Error de conexión")) as mock_connect:
        with pytest.raises(ConnectionError):
            conectar_db()

def test_crear_tablas():
    with mock.patch('conexion_bd.conectar_db') as mock_conectar_db:
        conexion_mock = mock.Mock()
        cursor_mock = mock.Mock()
        mock_conectar_db.return_value = (conexion_mock, cursor_mock)

        crear_tablas()
        assert cursor_mock.execute.called
        assert conexion_mock.commit.called
        conexion_mock.close.assert_called_once()

    
    with mock.patch('conexion_bd.conectar_db') as mock_conectar_db:
        conexion_mock = mock.Mock()
        cursor_mock = mock.Mock()
        cursor_mock.execute.side_effect = ConnectionError("Error al crear tablas")
        mock_conectar_db.return_value = (conexion_mock, cursor_mock)

        with pytest.raises(ConnectionError):
            crear_tablas()
        conexion_mock.close.assert_called_once()  

def test_insertar_usuarios():
    with mock.patch('conexion_bd.conectar_db') as mock_conectar_db:
        conexion_mock = mock.Mock()
        cursor_mock = mock.Mock()
        mock_conectar_db.return_value = (conexion_mock, cursor_mock)

        insertar_usuarios("Juan", 25)
        cursor_mock.execute.assert_called_once_with("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ("Juan", 25))
        conexion_mock.commit.assert_called_once()
        conexion_mock.close.assert_called_once()

    with pytest.raises(ValueError):
        insertar_usuarios("", -1)


    with mock.patch('conexion_bd.conectar_db') as mock_conectar_db:
        conexion_mock = mock.Mock()
        cursor_mock = mock.Mock()
        cursor_mock.execute.side_effect = ConnectionError("Error al insertar usuario")
        mock_conectar_db.return_value = (conexion_mock, cursor_mock)

        with pytest.raises(ConnectionError):
            insertar_usuarios("Juan", 25)
        conexion_mock.close.assert_called_once()  

def test_insertar_empleados():
    with mock.patch('conexion_bd.conectar_db') as mock_conectar_db:
        conexion_mock = mock.Mock()
        cursor_mock = mock.Mock()
        mock_conectar_db.return_value = (conexion_mock, cursor_mock)

        insertar_empleados(3000, "ingeniero")
        cursor_mock.execute.assert_called_once_with("INSERT INTO empleados (salario, puesto) VALUES (%s, %s)", (3000, "ingeniero"))
        conexion_mock.commit.assert_called_once()
        conexion_mock.close.assert_called_once()

    with pytest.raises(ValueError):
        insertar_empleados(-3000, "")

   
    with mock.patch('conexion_bd.conectar_db') as mock_conectar_db:
        conexion_mock = mock.Mock()
        cursor_mock = mock.Mock()
        cursor_mock.execute.side_effect = ConnectionError("Error al insertar empleado")
        mock_conectar_db.return_value = (conexion_mock, cursor_mock)

        with pytest.raises(ConnectionError):
            insertar_empleados(3000, "ingeniero")
        conexion_mock.close.assert_called_once()  

def test_insertar_clientes():
    with mock.patch('conexion_bd.conectar_db') as mock_conectar_db:
        conexion_mock = mock.Mock()
        cursor_mock = mock.Mock()
        mock_conectar_db.return_value = (conexion_mock, cursor_mock)

        insertar_clientes("Pedro", "Madrid")
        cursor_mock.execute.assert_called_once_with("INSERT INTO clientes (nombre, ciudad) VALUES (%s, %s)", ("Pedro", "Madrid"))
        conexion_mock.commit.assert_called_once()
        conexion_mock.close.assert_called_once()

    with pytest.raises(ValueError):
        insertar_clientes("", "")

  
    with mock.patch('conexion_bd.conectar_db') as mock_conectar_db:
        conexion_mock = mock.Mock()
        cursor_mock = mock.Mock()
        cursor_mock.execute.side_effect = ConnectionError("Error al insertar cliente")
        mock_conectar_db.return_value = (conexion_mock, cursor_mock)

        with pytest.raises(ConnectionError):
            insertar_clientes("Pedro", "Madrid")
        conexion_mock.close.assert_called_once()  

def test_insertar_pedidos():
    with mock.patch('conexion_bd.conectar_db') as mock_conectar_db:
        conexion_mock = mock.Mock()
        cursor_mock = mock.Mock()
        mock_conectar_db.return_value = (conexion_mock, cursor_mock)

        insertar_pedidos(1)
        cursor_mock.execute.assert_called_once_with("INSERT INTO pedidos (cliente_id) VALUES (%s)", (1,))
        conexion_mock.commit.assert_called_once()
        conexion_mock.close.assert_called_once()

    with pytest.raises(ValueError):
        insertar_pedidos(-1)


    with mock.patch('conexion_bd.conectar_db') as mock_conectar_db:
        conexion_mock = mock.Mock()
        cursor_mock = mock.Mock()
        cursor_mock.execute.side_effect = ConnectionError("Error al insertar pedido")
        mock_conectar_db.return_value = (conexion_mock, cursor_mock)

        with pytest.raises(ConnectionError):
            insertar_pedidos(1)
        conexion_mock.close.assert_called_once()  

def test_insertar_ventas():
    with mock.patch('conexion_bd.conectar_db') as mock_conectar_db:
        conexion_mock = mock.Mock()
        cursor_mock = mock.Mock()
        mock_conectar_db.return_value = (conexion_mock, cursor_mock)

        insertar_ventas("Producto A")
        cursor_mock.execute.assert_called_once_with("INSERT INTO ventas (producto) VALUES (%s)", ("Producto A",))
        conexion_mock.commit.assert_called_once()
        conexion_mock.close.assert_called_once()

    with pytest.raises(ValueError):
        insertar_ventas("")

    
    with mock.patch('conexion_bd.conectar_db') as mock_conectar_db:
        conexion_mock = mock.Mock()
        cursor_mock = mock.Mock()
        cursor_mock.execute.side_effect = ConnectionError("Error al insertar venta")
        mock_conectar_db.return_value = (conexion_mock, cursor_mock)

        with pytest.raises(ConnectionError):
            insertar_ventas("Producto A")
        conexion_mock.close.assert_called_once()  

