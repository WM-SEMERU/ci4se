def flux_v2(v_vars: List[fl.Var], i: int):
    k = 3 * i
    return fl.square(v_vars[k + 0]) + fl.square(v_vars[k + 1]) + fl.square(
        v_vars[k + 2])