def p_statements(p):
    """statements : statement
    | statements statement"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_statement(p):
    """statement : data_declaration
    | expression
    | if_statement
    """
    p[0] = p[1]


# | object_call


def p_data_declaration(p):
    """data_declaration : IDENTIFIER EQUALS expression"""
    p[0] = ("data_declaration", p[1], p[3])


def p_expression(p):
    """expression : IDENTIFIER
    | all_datatypes
    | comparison_expression
    """
    p[0] = p[1]


def p_comparison_expression(p):
    """comparison_expression : expression GT expression
    | expression LT expression
    | expression EQEQ expression
    | expression NEQ expression
    | expression GE expression
    | expression LE expression"""

    match p[2]:
        case ">":
            p[0] = (">", p[1], p[3])
        case "<":
            p[0] = ("<", p[1], p[3])
        case "==":
            p[0] = ("==", p[1], p[3])
        case "!=":
            p[0] = ("!=", p[1], p[3])
        case ">=":
            p[0] = (">=", p[1], p[3])
        case "<=":
            p[0] = ("<=", p[1], p[3])
