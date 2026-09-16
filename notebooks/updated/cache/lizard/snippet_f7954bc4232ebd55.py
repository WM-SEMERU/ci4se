def logical_or(lhs, rhs):
    return _ufunc_helper(lhs, rhs, op.broadcast_logical_or, lambda x, y: 1 if
        x or y else 0, _internal._logical_or_scalar, None)