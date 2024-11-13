import psycopg2

def conectar_db():
    try:
        conexion = psycopg2.connect(
            dbname="prog_avanzada",
            user="postgres",
            password="lucas792002",  
            host="localhost",
            port="5432",
            options="-c client_encoding=UTF8"
        )
        conexion.set_client_encoding('UTF8')
        cursor = conexion.cursor()
        return conexion, cursor
    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None, None

def crear_tablas():
    conexion, cursor = conectar_db()
    if not conexion or not cursor:
        raise ConnectionError("No se pudo establecer conexión para crear tablas.")

    try:
        tablas = [
            '''
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                edad INTEGER
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS clientes (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                ciudad VARCHAR(100)
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS empleados (
                id SERIAL PRIMARY KEY,
                salario INTEGER,
                puesto VARCHAR(100)
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS pedidos (
                id SERIAL PRIMARY KEY,
                cliente_id INTEGER REFERENCES clientes(id)
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS ventas (
                id SERIAL PRIMARY KEY,
                producto VARCHAR(100)
            )
            '''
        ]

        for tabla in tablas:
            cursor.execute(tabla)
        conexion.commit()
        print("Tablas creadas con éxito.")
    except psycopg2.Error as e:
        print(f"Error al crear tablas: {e}")
        raise ConnectionError("Error al crear tablas en la base de datos.")
    finally:
        if conexion:
            conexion.close()

def insertar_usuarios(nombre, edad):
    if not nombre or edad is None or edad < 0:
        raise ValueError("Parámetros inválidos para la inserción de usuarios.")
    conexion, cursor = conectar_db()
    if not conexion or not cursor:
        raise ConnectionError("No se pudo establecer conexión para insertar usuarios.")

    try:
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", (nombre, edad))
        conexion.commit()
        print(f"Usuario insertado: {nombre}, {edad}")
    except psycopg2.Error as e:
        print(f"Error al insertar usuario: {e}")
        raise ConnectionError("Error al insertar usuario en la base de datos.")
    finally:
        if conexion:
            conexion.close()

def insertar_empleados(salario, puesto):
    if salario is None or salario < 0 or not puesto:
        raise ValueError("Parámetros inválidos para la inserción de empleados.")
    conexion, cursor = conectar_db()
    if not conexion or not cursor:
        raise ConnectionError("No se pudo establecer conexión para insertar empleados.")

    try:
        cursor.execute("INSERT INTO empleados (salario, puesto) VALUES (%s, %s)", (salario, puesto))
        conexion.commit()
        print(f"Empleado insertado: {salario}, {puesto}")
    except psycopg2.Error as e:
        print(f"Error al insertar empleado: {e}")
        raise ConnectionError("Error al insertar empleado en la base de datos.")
    finally:
        if conexion:
            conexion.close()

def insertar_clientes(nombre, ciudad):
    if not nombre or not ciudad:
        raise ValueError("Parámetros inválidos para la inserción de clientes.")
    conexion, cursor = conectar_db()
    if not conexion or not cursor:
        raise ConnectionError("No se pudo establecer conexión para insertar clientes.")

    try:
        cursor.execute("INSERT INTO clientes (nombre, ciudad) VALUES (%s, %s)", (nombre, ciudad))
        conexion.commit()
        print(f"Cliente insertado: {nombre}, {ciudad}")
    except psycopg2.Error as e:
        print(f"Error al insertar cliente: {e}")
        raise ConnectionError("Error al insertar cliente en la base de datos.")
    finally:
        if conexion:
            conexion.close()

def insertar_pedidos(cliente_id):
    if cliente_id is None or cliente_id < 0:
        raise ValueError("Parámetros inválidos para la inserción de pedidos.")
    conexion, cursor = conectar_db()
    if not conexion or not cursor:
        raise ConnectionError("No se pudo establecer conexión para insertar pedidos.")

    try:
        cursor.execute("INSERT INTO pedidos (cliente_id) VALUES (%s)", (cliente_id,))
        conexion.commit()
        print(f"Pedido insertado para cliente ID: {cliente_id}")
    except psycopg2.Error as e:
        print(f"Error al insertar pedido: {e}")
        raise ConnectionError("Error al insertar pedido en la base de datos.")
    finally:
        if conexion:
            conexion.close()

def insertar_ventas(producto):
    if not producto:
        raise ValueError("Parámetros inválidos para la inserción de ventas.")
    conexion, cursor = conectar_db()
    if not conexion or not cursor:
        raise ConnectionError("No se pudo establecer conexión para insertar ventas.")

    try:
        cursor.execute("INSERT INTO ventas (producto) VALUES (%s)", (producto,))
        conexion.commit()
        print(f"Venta insertada: {producto}")
    except psycopg2.Error as e:
        print(f"Error al insertar venta: {e}")
        raise ConnectionError("Error al insertar venta en la base de datos.")
    finally:
        if conexion:
            conexion.close()

def ejecutar_consulta(consulta):
    if not consulta:
        raise ValueError("La consulta no puede estar vacía.")
    conexion, cursor = conectar_db()
    if not conexion or not cursor:
        raise ConnectionError("No se pudo establecer conexión para ejecutar la consulta.")

    resultados = []
    try:
        cursor.execute(consulta)
        if consulta.strip().upper().startswith("SELECT"):
            resultados = cursor.fetchall()
        conexion.commit()
        print("Consulta ejecutada con éxito.")
    except psycopg2.Error as e:
        print(f"Error al ejecutar consulta: {e}")
        raise ConnectionError("Error al ejecutar consulta en la base de datos.")
    finally:
        if conexion:
            conexion.close()

    return resultados


