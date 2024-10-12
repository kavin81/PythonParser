### Collection Types ###


def p_list_items(p):
    """list_items : all_datatypes COMMA list_items
    | all_datatypes
    | empty"""
    if len(p) == 2:
        p[0] = [p[1]]  # single expression
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]  # multiple expressions
    else:
        p[0] = []


def p_kv_list_items(p):
    """kv_list_items : kv COMMA kv_list_items
    | kv
    | empty"""
    if len(p) == 2:
        p[0] = [p[1]]  # single expression
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]  # multiple expressions
    else:
        p[0] = []


def p_kv(p):
    """kv : STRING  COLON all_datatypes
    | INT COLON all_datatypes"""
    p[0] = (p[1], p[3])


### Collections ###


# [a, b, c]
def p_list(p):
    """list : LBRACKET list_items RBRACKET"""
    p[0] = ("list", p[2])


# (a, b, c)
def p_tuple(p):
    """tuple : LPAREN list_items RPAREN"""
    p[0] = ("tuple", p[2])


# {a, b, c}
def p_set(p):
    """set : LBRACE list_items RBRACE"""
    p[0] = ("set", p[2])


# {a: b, c: d}
def p_dict(p):
    """dict : LBRACE kv_list_items RBRACE"""
    p[0] = ("dict", p[2])


def p_basic_datatype(p):
    """basic_datatype : INT
    | FLOAT
    | STRING
    | BOOL"""
    p[0] = p[1]


def p_all_datatypes(p):
    """all_datatypes : collection
    | basic_datatype
    """
    p[0] = p[1]


# | object_call


def p_collection(p):
    """collection : list
    | tuple
    | dict
    | set"""
    p[0] = p[1]


### Typehinting / Typecasting ###


def p_typehint_type(p):
    """typehint_type : COLON TYPE_INT
    | TYPE_FLOAT
    | TYPE_STRING
    | TYPE_BOOL
    | TYPE_LIST
    | TYPE_TUPLE
    | TYPE_DICT
    | TYPE_SET"""
    p[0] = p[2]


def p_typehint(p):
    """typehint : COLON typehint_type
    | empty"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None
