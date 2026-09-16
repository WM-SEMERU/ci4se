def _FullEOM(y, t, pot):
    l2 = (y[0] ** 2.0 * y[3]) ** 2.0
    return [y[1], l2 / y[0] ** 3.0 + _evaluateRforces(pot, y[0], y[4], phi=
        y[2], t=t, v=[y[1], y[0] * y[3], y[5]]), y[3], 1.0 / y[0] ** 2.0 *
        (_evaluatephiforces(pot, y[0], y[4], phi=y[2], t=t, v=[y[1], y[0] *
        y[3], y[5]]) - 2.0 * y[0] * y[1] * y[3]), y[5], _evaluatezforces(
        pot, y[0], y[4], phi=y[2], t=t, v=[y[1], y[0] * y[3], y[5]])]