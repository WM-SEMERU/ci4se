def countedArray(expr, intExpr=None):
    arrayExpr = Forward()

    def countFieldParseAction(s, l, t):
        n = t[0]
        arrayExpr << (n and Group(And([expr] * n)) or Group(empty))
        return []
    if intExpr is None:
        intExpr = Word(nums).setParseAction(lambda t: int(t[0]))
    else:
        intExpr = intExpr.copy()
    intExpr.setName('arrayLen')
    intExpr.addParseAction(countFieldParseAction, callDuringTry=True)
    return intExpr + arrayExpr