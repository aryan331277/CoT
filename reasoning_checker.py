from sympy import simplify, parse_expr
from z3 import Solver, Implies, And, Or, Not, Bool, sat

def check_math_step(step):
    try:
        if '=' in step:
            lhs, rhs = step.split('=')
            lhs_expr = simplify(parse_expr(lhs.strip()))
            rhs_expr = simplify(parse_expr(rhs.strip()))
            return lhs_expr == rhs_expr
        else:
            simplified = simplify(parse_expr(step.strip()))
            return simplified.is_zero
    except:
        return False

def check_logic_step(step):
    s = Solver()
    try:
        expr = eval(
            step.replace("=>", ",").replace("&", ","),
            {"Implies": Implies, "And": And, "Or": Or, "Not": Not, "Bool": Bool}
        )
        s.add(expr)
        return s.check() == sat
    except:
        return False
