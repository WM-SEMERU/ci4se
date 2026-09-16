def parse_arglist(args):
    args = 'f({})'.format(args)
    tree = ast.parse(args)
    funccall = tree.body[0].value
    args = [ast.literal_eval(arg) for arg in funccall.args]
    kwargs = {arg.arg: ast.literal_eval(arg.value) for arg in funccall.keywords
        }
    if len(args) > 2:
        raise TypeError('Expected at most 2 positional args but {} were given'
            .format(len(args)))
    if len(args) >= 1:
        kwargs['width'] = int(args[0])
    if len(args) >= 2:
        kwargs['height'] = int(args[1])
    return kwargs