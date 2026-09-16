def is_SYMBOL(token, *symbols):
    from symbols.symbol_ import Symbol
    assert all(isinstance(x, Symbol) for x in symbols)
    for sym in symbols:
        if sym.token != token:
            return False
    return True