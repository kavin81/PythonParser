from rich.pretty import pprint


def p_empty(p):
    """empty :"""
    p[0] = []


def p_error(p):
    if p:
        pprint(
            f"\nSyntax error at line {p.lineno}, position {p.lexpos}, token {p.type}, value {p.value}"
        )

    else:
        print("Syntax error at EOF")


__all__ = ["p_empty", "p_error"]
