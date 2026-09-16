def concatenate(*args, **kwargs):
    divider = kwargs.get('divider', '')
    result = ''
    for arg in args:
        if result == '':
            result += arg
        else:
            result += '{0}{1}'.format(divider, arg)
    return result