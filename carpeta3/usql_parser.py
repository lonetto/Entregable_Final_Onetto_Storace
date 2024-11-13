import ply.yacc as yacc
from usql_lexer import tokens

def p_statement(t):
    '''statement : statement token
                 | token
                 | statement SEMICOLON
                 | token SEMICOLON'''
    if len(t) == 3 and t[2] != ';': 
        t[0] = f"{t[1]} {t[2]}"
    else:
        t[0] = t[1]  

def p_token(t):
    '''token : WORD
             | NUMBER
             | GT
             | LT
             | EQ
             | STRING
             | LPAREN
             | RPAREN
             | COMMA
             | ASTERISK
             | DOT'''
    t[0] = str(t[1])


def p_error(t):
    if t:
        print(f"Error sintáctico: {t}")
    else:
        print("Error de sintaxis al final de la entrada")

parser = yacc.yacc()


def parse_input(data):
    result = parser.parse(data)
    return result


if __name__ == "__main__":
    consultas_usql = [
        "TRAEME TODO DE_LA_TABLA usuarios DONDE edad > 18;",
        "METE_EN usuarios (nombre, edad) LOS_VALORES ('Juan', 25);",
        "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';",
        "BORRA_DE_LA_TABLA clientes DONDE edad > 30;"
    ]

    for consulta in consultas_usql:
        resultado = parse_input(consulta)
        print(resultado)

