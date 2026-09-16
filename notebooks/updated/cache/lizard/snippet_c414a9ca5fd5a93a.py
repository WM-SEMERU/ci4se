def parse_float_literal(ast, _variables=None):
    if isinstance(ast, (FloatValueNode, IntValueNode)):
        return float(ast.value)
    return INVALID