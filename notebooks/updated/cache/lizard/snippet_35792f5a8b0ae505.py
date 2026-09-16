def list(context, sort, limit, where, verbose):
    result = product.list(context, sort=sort, limit=limit, where=where)
    utils.format_output(result, context.format, verbose=verbose)