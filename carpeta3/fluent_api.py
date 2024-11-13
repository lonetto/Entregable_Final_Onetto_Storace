from conexion_bd import (
    insertar_usuarios, insertar_empleados, insertar_clientes,
    insertar_pedidos, insertar_ventas
)

class FluentQueryBuilder:
    def __init__(self):
        self.query_parts = []

    def _validar_no_vacio(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)

    def _validar_tipo(self, valor, tipo, mensaje):
        if not isinstance(valor, tipo):
            raise TypeError(mensaje)

    def traeme(self, *args):
        self._validar_no_vacio(args, "Debe especificar al menos una columna para seleccionar.")
        self.query_parts.append(f"TRAEME {', '.join(args)}")
        return self

    def de_la_tabla(self, table_name):
        self._validar_no_vacio(table_name, "El nombre de la tabla no puede estar vacío.")
        self.query_parts.append(f"DE_LA_TABLA {table_name}")
        return self

    def donde(self, condition):
        self._validar_no_vacio(condition, "La condición no puede estar vacía.")
        self.query_parts.append(f"DONDE {condition}")
        return self

    def agrupando_por(self, *args):
        self._validar_no_vacio(args, "Debe especificar al menos una columna para agrupar.")
        self.query_parts.append(f"AGRUPANDO_POR {', '.join(args)}")
        return self

    def mezclando(self, table_name):
        self._validar_no_vacio(table_name, "El nombre de la tabla a mezclar no puede estar vacío.")
        self.query_parts.append(f"MEZCLANDO {table_name}")
        return self

    def en(self, condition):
        self._validar_no_vacio(condition, "La condición para la mezcla no puede estar vacía.")
        self.query_parts.append(f"EN {condition}")
        return self

    def los_distintos(self, *args):
        self._validar_no_vacio(args, "Debe especificar al menos una columna para seleccionar.")
        self.query_parts.append(f"LOS_DISTINTOS {', '.join(args)}")
        return self

    def mete_en(self, table_name, *args):
        self._validar_no_vacio(table_name, "El nombre de la tabla no puede estar vacío.")
        self._validar_no_vacio(args, "Los valores no pueden ser None.")
        self.query_parts.append(f"METE_EN {table_name} ({', '.join(args)})")
        return self

    def los_valores(self, *args):
        self._validar_no_vacio(args, "Los valores no pueden ser None.")
        self.query_parts.append(f"LOS_VALORES ({', '.join(args)})")
        return self

    def actualiza(self, table_name):
        self._validar_no_vacio(table_name, "El nombre de la tabla para actualizar no puede estar vacío.")
        self.query_parts.append(f"ACTUALIZA {table_name}")
        return self

    def setea(self, update_statement):
        self._validar_no_vacio(update_statement, "La sentencia de actualización no puede estar vacía.")
        self.query_parts.append(f"SETEA {update_statement}")
        return self

    def borra_de_la(self, table_name):
        self._validar_no_vacio(table_name, "El nombre de la tabla no puede estar vacío.")
        self.query_parts.append(f"BORRA_DE_LA_TABLA {table_name}")
        return self

    def ordena_por(self, *args):
        self._validar_no_vacio(args, "Debe especificar al menos una columna para ordenar.")
        self.query_parts.append(f"ORDENA_POR {', '.join(args)}")
        return self

    def como_mucho(self, limit):
        self._validar_tipo(limit, int, "El límite debe ser un número entero.")
        if limit <= 0:
            raise ValueError("El límite debe ser un número entero positivo.")
        self.query_parts.append(f"COMO_MUCHO {limit}")
        return self

    def existe(self):
        self.query_parts.append("EXISTE")
        return self

    def en_esto(self, condition):
        self._validar_no_vacio(condition, "La condición no puede estar vacía.")
        self.query_parts.append(f"EN_ESTO: {condition}")
        return self

    def entre(self, lower_bound, upper_bound):
        if lower_bound is None or upper_bound is None:
            raise ValueError("Los límites no pueden ser None.")
        self.query_parts.append(f"ENTRE {lower_bound} Y {upper_bound}")
        return self

    def parecido_a(self, pattern):
        self._validar_no_vacio(pattern, "El patrón no puede estar vacío.")
        self.query_parts.append(f"PARECIDO_A '{pattern}'")
        return self

    def es_nulo(self):
        self.query_parts.append("ES_NULO")
        return self

 
    def insertar_usuarios(self, nombre, edad):
        self._validar_no_vacio(nombre, "El nombre no puede estar vacío.")
        self._validar_tipo(edad, int, "La edad debe ser un número entero.")
        insertar_usuarios(nombre, edad)
        return self

    def insertar_empleados(self, salario, puesto):
        self._validar_tipo(salario, int, "El salario debe ser un número entero.")
        self._validar_no_vacio(puesto, "El puesto no puede estar vacío.")
        insertar_empleados(salario, puesto)
        return self

    def insertar_clientes(self, nombre, ciudad):
        self._validar_no_vacio(nombre, "El nombre no puede estar vacío.")
        self._validar_no_vacio(ciudad, "La ciudad no puede estar vacía.")
        insertar_clientes(nombre, ciudad)
        return self

    def insertar_pedidos(self, cliente_id):
        self._validar_tipo(cliente_id, int, "El ID del cliente debe ser un número entero.")
        insertar_pedidos(cliente_id)
        return self

    def insertar_ventas(self, producto):
        self._validar_no_vacio(producto, "El producto no puede estar vacío.")
        insertar_ventas(producto)
        return self

    def construir(self):
        if not self.query_parts:
            raise ValueError("No se ha construido ninguna parte de la consulta.")
        return ' '.join(self.query_parts).strip()
