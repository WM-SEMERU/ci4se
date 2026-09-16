def Eoi(compiler, cont):
    return il.If(il.Ge(il.GetItem(il.parse_state, il.Integer(1)), il.Len(il
        .GetItem(il.parse_state, il.Integer(0)))), cont(TRUE), il.failcont(
        FALSE))