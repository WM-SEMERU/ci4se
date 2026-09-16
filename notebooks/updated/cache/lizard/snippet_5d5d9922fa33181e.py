def create_node(t, ref=None, debug=False):
    if t.ttype == 'operand':
        if t.tsubtype in ['range', 'named_range', 'pointer']:
            return RangeNode(t, ref, debug=debug)
        else:
            return OperandNode(t)
    elif t.ttype == 'function':
        return FunctionNode(t, ref, debug=debug)
    elif t.ttype.startswith('operator'):
        return OperatorNode(t, ref, debug=debug)
    else:
        return ASTNode(t, debug=debug)