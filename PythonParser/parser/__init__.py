import ply.yacc as yacc
from ..lexer.tokens import tokens


from .util import *
from .statements import *
from .root import *
from .types import *

from .statements import *
from .oop import *


parser = yacc.yacc(debug=True, outputdir="./build")
