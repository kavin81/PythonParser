import ply.lex as lex
from .tokens import tokens, reserved

# brackets
t_LPAREN, t_RPAREN = r"\(", r"\)"
t_LBRACKET, t_RBRACKET = r"\[", r"\]"
t_LBRACE, t_RBRACE = r"\{", r"\}"
# common symbols
t_COLON = r":"
t_COMMA = r","
# selection statements
t_IF, t_ELSE, t_ELIF = r"if", r"else", r"elif"

# assignment operator
t_EQUALS = r"="
# comparison operators
t_EQEQ = r"=="
t_NEQ = r"!="
t_GT = r">"
t_GE = r">="
t_LT = r"<"
t_LE = r"<="
# type casting & literals
t_TYPE_INT = r"int"
t_TYPE_FLOAT = r"float"
t_TYPE_BOOL = r"bool"
t_TYPE_STRING = r"str"
t_TYPE_LIST = r"list"
t_TYPE_DICT = r"dict"
t_TYPE_SET = r"set"
t_TYPE_TUPLE = r"tuple"

# OOP
t_DEF = r"def"
t_CLASS = r"class"
t_RETURN = r"return"


def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "IDENTIFIER")
    return t


def t_FLOAT(t):
    r"[-+]?\d+\.\d*([eE][-+]?\d+)?"
    t.value = float(t.value)
    return t


def t_INT(t):
    r"[-+]?\d+"
    t.value = int(t.value)
    return t


def t_BOOL(t):
    r"(True|False)"
    t.value = True if t.value == "True" else False
    return t


def t_STRING(t):
    r"\"(.*?)\"|\'(.*?)\'"
    t.value = str(t.value[1:-1])
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = " \t"


def t_error(t):
    print(
        f"Syntax error at line {t.lineno}, position {t.lexpos}, token {t.type}, value {t.value}"
    )
    t.lexer.skip(1)
