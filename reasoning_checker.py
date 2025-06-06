from sympy import simplify, Eq, symbols
from sympy.parsing.sympy_parser import parse_expr
from z3 import Solver, Bool, And, Or, Not, Implies, sat

def check_math_step(step):
    try:
        x = symbols('x')
        if '=' in step:
            lhs, rhs = step.split('=')
            expr = simplify(parse_expr(lhs) - parse_expr(rhs))
            return expr == 0
        else:
            simplified = simplify(parse_expr(step))
            return bool(simplified)
    except:
        return False

def check_logic_step(step):
    try:
        s = Solver()
        A, B, C = Bool('A'), Bool('B'), Bool('C')
        logic_expr = eval(step.replace("=>", "Implies").replace("&", "And").replace("|", "Or").replace("~", "Not"))
        s.add(logic_expr)
        return s.check() == sat
    except:
        return False
