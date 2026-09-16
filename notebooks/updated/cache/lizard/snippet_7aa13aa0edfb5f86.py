def resolve(input, representation, resolvers=None, **kwargs):
    resultdict = query(input, representation, resolvers, **kwargs)
    result = resultdict[0]['value'] if resultdict else None
    if result and len(result) == 1:
        result = result[0]
    return result