def ContextTupleToDict(context):
    d = {}
    if not context:
        return d
    for k, v in zip(ExceptionWithContext.CONTEXT_PARTS, context):
        if v != '' and v != None:
            d[k] = v
    return d