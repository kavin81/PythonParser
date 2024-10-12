def p_if_statement(p):
    """if_statement : IF expression COLON statements elif_else_block"""

    # Accumulate the entire if-elif-else structure into a list
    p[0] = [("if", p[2], p[4])] + p[5]  # p[5] contains elif/else blocks


def p_elif_else_block(p):
    """elif_else_block : ELIF expression COLON statements elif_else_block
    | ELSE COLON statements
    | empty"""

    if len(p) == 6:  # Elif block
        p[0] = [("elif", p[2], p[4])] + p[5]
    elif len(p) == 4:  # Else block
        p[0] = [("else", p[3])]
    else:  # Empty block (for no elif/else)
        p[0] = []
