def Montinsky(P, Pc, Te=None, q=None):
    r
    if Te:
        return (0.00417 * (Pc / 1000.0) ** 0.69 * Te ** 0.7 * (1.8 * (P /
            Pc) ** 0.17 + 4 * (P / Pc) ** 1.2 + 10 * (P / Pc) ** 10)) ** (1 /
            0.3)
    elif q:
        return 0.00417 * (Pc / 1000.0) ** 0.69 * q ** 0.7 * (1.8 * (P / Pc) **
            0.17 + 4 * (P / Pc) ** 1.2 + 10 * (P / Pc) ** 10)
    else:
        raise Exception('Either q or Te is needed for this correlation')