def __or(funcs, args):
    results = []
    for f in funcs:
        result = f(args)
        if result:
            results.extend(result)
    return results