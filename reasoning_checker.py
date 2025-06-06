# reasoning_checker.py

from sympy import *
from z3 import Solver, parse_smt2_string

def check_math_step(step):
    try:
        expr = parse_expr(step.replace('=', 'Eq'))
        if 'Eq' in str(expr):
            lhs, rhs = expr.lhs, expr.rhs
            simplified = simplify(lhs - rhs)
            return simplified == 0
        else:
            simplified = simplify(expr)
            return simplified
    except:
        return False

def check_logic_step(step):
    s = Solver()
    try:
        expr = eval(step.replace("=>", "Implies").replace("&", "And"))
        s.add(expr)
        return s.check() == sat
    except:
        return False
