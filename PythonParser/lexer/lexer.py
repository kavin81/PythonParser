# lexer.py
import ply.lex as lex
from .tokens import tokens
from .rules import *

lexer = lex.lex()

__all__ = ["lexer", "tokens"]
