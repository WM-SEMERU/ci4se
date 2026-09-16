def RACC_calc(TOP, P, POP):
    try:
        result = TOP * P / POP ** 2
        return result
    except Exception:
        return 'None'