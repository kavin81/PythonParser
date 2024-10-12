tokens = (
    # operands
    "IDENTIFIER",
    # assignment operator
    "EQUALS",
    # Comparison operators
    "EQEQ",
    "GT",
    "GE",
    "LT",
    "LE",
    "NEQ",
    # brackets
    # ()
    "LPAREN",
    "RPAREN",
    # []
    "LBRACKET",
    "RBRACKET",
    # {}
    "LBRACE",
    "RBRACE",
    # symbols
    "COLON",
    "COMMA",
    # literals
    "FLOAT",
    "INT",
    "BOOL",
    "STRING",
    # type casting & literals
    "TYPE_INT",
    "TYPE_FLOAT",
    "TYPE_BOOL",
    "TYPE_STRING",
    "TYPE_LIST",
    "TYPE_DICT",
    "TYPE_SET",
    "TYPE_TUPLE",
    # selection statements
    "IF",
    "ELSE",
    "ELIF",
    # OOP
    "DEF",
    "CLASS",
    "RETURN",
)

reserved = {
    # selection statements
    "if": "IF",
    "else": "ELSE",
    "elif": "ELIF",
    # types
    "True": "BOOL",
    "False": "BOOL",
    # type casting & literals
    "int": "TYPE_INT",
    "float": "TYPE_FLOAT",
    "bool": "TYPE_BOOL",
    "str": "TYPE_STRING",
    "list": "TYPE_LIST",
    "dict": "TYPE_DICT",
    "set": "TYPE_SET",
    "tuple": "TYPE_TUPLE",
    # OOP
    "def": "DEF",
    "class": "CLASS",
    "return": "RETURN",
}


__all__ = ["tokens", "reserved"]
