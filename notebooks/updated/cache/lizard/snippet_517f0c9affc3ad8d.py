def make_node(cls, *args):
    new_args = []
    args = [x for x in args if not is_null(x)]
    for x in args:
        assert isinstance(x, Symbol)
        if x.token == 'BLOCK':
            new_args.extend(SymbolBLOCK.make_node(*x.children).children)
        else:
            new_args.append(x)
    result = SymbolBLOCK(*new_args)
    return result