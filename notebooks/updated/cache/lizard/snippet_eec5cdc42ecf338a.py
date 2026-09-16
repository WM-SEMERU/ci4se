def _is_referenced_in_argv(method_name):
    expr = '.*[:.]{0}$'.format(method_name)
    regex = re.compile(expr)
    return any(regex.match(arg) for arg in sys.argv)