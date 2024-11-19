def occurs_check(var, expr, substitution):
    if var == expr:
        return True
    elif isinstance(expr, list):
        return any(occurs_check(var, sub_expr, substitution) for sub_expr in expr)
    elif expr in substitution:
        return occurs_check(var, substitution[expr], substitution)
    return False

def unify_variable(var, expr, substitution):
    if var in substitution:
        return unify(substitution[var], expr, substitution)
    elif expr in substitution:
        return unify(var, substitution[expr], substitution)
    elif occurs_check(var, expr, substitution):
        raise ValueError(f"Occurs check failed: {var} occurs in {expr}")
    else:
        substitution[var] = expr
        return substitution

def unify(expr1, expr2, substitution=None):
    if substitution is None:
        substitution = {}

    to_unify = [(expr1, expr2)]

    while to_unify:
        x, y = to_unify.pop(0)

        if x == y:
            continue

        if isinstance(x, str) and x.islower():
            substitution = unify_variable(x, y, substitution)
        elif isinstance(y, str) and y.islower():
            substitution = unify_variable(y, x, substitution)
        elif isinstance(x, list) and isinstance(y, list):
            if len(x) != len(y):
                raise ValueError(f"Cannot unify terms with different arities: {x}, {y}")
            to_unify.extend(zip(x, y))
        else:
            raise ValueError(f"Unification failed for terms: {x}, {y}")

    return substitution

if __name__ == "__main__":
    expr1 = ["f", "x", "a"]
    expr2 = ["f", "b", "y"]

    try:
        result = unify(expr1, expr2)
        print("Unifier:", result)
    except ValueError as e:
        print("Unification failed:", e)
