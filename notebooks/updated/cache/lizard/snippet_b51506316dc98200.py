def ComplementMembership(*args, **kwargs):
    return ast.Complement(ast.Membership(*args, **kwargs), **kwargs)