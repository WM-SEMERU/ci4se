def power(base, exp):
    return _ufunc_helper(base, exp, op.broadcast_power, operator.pow,
        _internal._power_scalar, _internal._rpower_scalar)