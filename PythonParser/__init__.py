from .lexer import lexer
from rich.console import Console
from rich.panel import Panel
from rich.pretty import Pretty
from .parser import parser


def parse(code):
    lexer.input(code)
    tokens = []

    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)

    console = Console()
    console.print(Panel.fit(Pretty(tokens), title="Parsed Tokens"))

    return parser.parse(code)
