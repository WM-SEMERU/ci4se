def NIR_calc(P, POP):
    try:
        max_P = max(list(P.values()))
        length = POP
        return max_P / length
    except Exception:
        return 'None'