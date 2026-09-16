def omega(imps):
    if isinstance(imps, v_Us_dict):
        return sum([omega(V) for U, V in imps.items()])
    if isinstance(imps, list):
        return sum([omega(x) for x in imps])
    if isinstance(imps, str):
        try:
            U, V = imps.split('->')
            Us = U.split(',') if ',' in U else U.split()
            Vs = V.split(',') if ',' in V else V.split()
            res = len(Us) * len(Vs)
            return res
        except:
            return 0
    if isinstance(imps, int):
        b = bin(imps)[2:]
        res = len([x for x in b if x == '1'])
        return res