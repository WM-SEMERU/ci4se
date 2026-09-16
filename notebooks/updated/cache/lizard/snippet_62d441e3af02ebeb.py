def __Calc_HSL_to_RGB_Components(var_q, var_p, C):
    if C < 0:
        C += 1.0
    if C > 1:
        C -= 1.0
    if C < 1.0 / 6.0:
        return var_p + (var_q - var_p) * 6.0 * C
    elif 1.0 / 6.0 <= C < 0.5:
        return var_q
    elif 0.5 <= C < 2.0 / 3.0:
        return var_p + (var_q - var_p) * 6.0 * (2.0 / 3.0 - C)
    else:
        return var_p