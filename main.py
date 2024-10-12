"""
__author__ = "Kavin S, M V Chinmay"

"""

from PythonParser import parse

from rich import print
from rich.pretty import Pretty
from rich.panel import Panel


def main():

    basic_types = """
    type_integer = 3
    type_float = 3.14
    type_str = "hello"
    type_bool = True
    """

    arr_types = """
    type_list = [1, 2, 3]
    type_tuple = (1, 2, 3)
    type_dict = {"a": 1, "b": 2, "c": 3}
    type_list_nested = [1, 2, [3, 4, [5, 6]]]
    """

    selection_statements = """
    if x:
        x = 1
    elif y:
        y = 2
    else:
        z = 3
    """

    code = basic_types + arr_types + selection_statements

    parsed_code = parse(code)
    print(
        Panel.fit(
            Pretty(parsed_code),
            title="Parsed Code",
        ),
    )


if __name__ == "__main__":
    main()
