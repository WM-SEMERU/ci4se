def get_role(member, cython=False):
    if inspect.isroutine(member) or isinstance(member, numpy.ufunc):
        return 'func'
    elif inspect.isclass(member):
        return 'class'
    elif cython:
        return 'func'
    return 'const'