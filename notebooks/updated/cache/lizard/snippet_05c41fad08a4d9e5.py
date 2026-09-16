def an(op, ac=None, rc=None, r=None, rr=None):
    return CONN.AssociatorNames(op, AssocClass=ac, ResultClass=rc, Role=r,
        ResultRole=rr)