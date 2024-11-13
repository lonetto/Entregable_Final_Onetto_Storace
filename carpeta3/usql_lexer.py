import ply.lex as lex


usql_to_sql = {
    "TRAEME": "SELECT",
    "TODO": "*",
    "DE_LA_TABLA": "FROM",
    "DONDE": "WHERE",
    "AGRUPANDO_POR": "GROUP BY",
    "MEZCLANDO": "JOIN",
    "EN": "ON",
    "LOS_DISTINTOS": "DISTINCT",
    "CONTANDO": "COUNT",
    "METE_EN": "INSERT INTO",
    "LOS_VALORES": "VALUES",
    "ACTUALIZA": "UPDATE",
    "SETEA": "SET",
    "BORRA_DE_LA_TABLA": "DELETE FROM",
    "ORDENA_POR": "ORDER BY",
    "COMO_MUCHO": "LIMIT",
    "WHERE_DEL_GROUP_BY": "HAVING",
    "EXISTE": "EXISTS",
    "EN_ESTO:": "IN",
    "ENTRE": "BETWEEN",
    "PARECIDO_A": "LIKE",
    "ES_NULO": "IS NULL",
    "CAMBIA_LA_TABLA": "ALTER TABLE",
    "AGREGA_LA_COLUMNA": "ADD COLUMN",
    "ELIMINA_LA_COLUMNA": "DROP COLUMN",
    "CREA_LA_TABLA": "CREATE TABLE",
    "TIRA_LA_TABLA": "DROP TABLE",
    "POR_DEFECTO": "DEFAULT",
    "UNICO": "UNIQUE",
    "CLAVE_PRIMA": "PRIMARY KEY",
    "CLAVE_REFERENTE": "FOREIGN KEY",
    "NO_NULO": "NOT NULL",
    "TRANSFORMA_A": "CAST",
    "Y": "AND",
}


tokens = [
    'WORD', 'GT', 'LT', 'EQ', 'NUMBER', 'STRING', 'LPAREN', 'RPAREN',
    'COMMA', 'ASTERISK', 'DOT', 'SEMICOLON'
]


t_ignore = ' \t'

t_GT = r'>'
t_LT = r'<'
t_EQ = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ASTERISK = r'\*'
t_DOT = r'\.'
t_SEMICOLON = r';'  

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\'[^\']*\''
    t.value = t.value[1:-1]  
    return t


def t_WORD(t):
    r'\w+'
    t.value = usql_to_sql.get(t.value.upper(), t.value.upper())  
    return t


def t_error(t):
    print(f"Error léxico: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()


def lex_input(data):
    lexer.input(data)
    return list(lexer)
