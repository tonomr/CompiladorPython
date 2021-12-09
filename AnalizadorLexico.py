import ply.lex as lex

RESERVADAS = ['BEGIN','END','IF','THEN','WHILE','DO','CALL','CONST','VAR','PROCEDURE','OUT','IN','ELSE']
tokens = RESERVADAS + ['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE','ODD','ASSIGN','NE','LT','LTE','GT','GTE','LPARENT', 'RPARENT','COMMA','SEMMICOLOM','DOT','UPDATE']

t_ignore = '\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='


def t_ID(token):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if token.value.upper() in RESERVADAS:
		token.value = token.value.upper()
		token.type = token.value
	return token


def t_newline(token):
	r'\n+'
	token.lexer.lineno += len(token.value)


def t_COMMENT(token):
	r'\#.*'
	pass


def t_NUMBER(token):
	r'\d+'
	token.value = int(token.value)
	return token


def t_error(token):
	print('Caracter No Reconocido {token.value[0]}')
	token.lexer.skip(1)


analizador = lex.lex()

# El programa Lee el archivo de texto (que es un programa en lenguaje PL/0)
# Y detecta e imprime todos los tokens que pertenecen al lenguaje
