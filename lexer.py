import ply.lex as lex

tokens = ('INT', 'ID', 'SEMI_COLON', 'EQUAL', 'WHILE', 'L_PARENTHESIS', 'R_PARENTHESIS', 'L_CBRACES', 'R_CBRACES',
          'PLUS', 'MINUS', 'TIMES', 'DIVIDE','MOD','LOE', 'GOE', 'EQ', 'GREAT', 'LESS', 'NUMBER','COMMA','NEQ' ,'DO','TYPE'
          ,'IF','ELSE','FOR','TYPEDEF','STRUCT')

reserved = {
    'int': 'INT',
    'while': 'WHILE',
    'do':'DO',
    'int': 'TYPE',
    'char': 'TYPE',
    'float': 'TYPE',
    'double': 'TYPE',
    'if':'IF',
    'else':'ELSE',
    'for' : 'FOR',
    'typedef' : 'TYPEDEF',
    'struct' : 'STRUCT',
}

t_ignore = ' \t\n' 
t_SEMI_COLON = r';'
t_EQUAL = r'='
t_COMMA = r','
t_L_PARENTHESIS = r'\('
t_R_PARENTHESIS = r'\)'
t_L_CBRACES = r'\{'
t_R_CBRACES = r'\}'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LOE = r'<='
t_GOE = r'>='
t_EQ = r'=='
t_GREAT = r'>'
t_LESS = r'<'
t_NUMBER = r'\d+'
t_NEQ=r'!='
t_TYPE = r'int|char|float|double'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()
