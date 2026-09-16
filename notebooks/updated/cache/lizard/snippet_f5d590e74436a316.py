def canparse(argparser, args):
    old_error_method = argparser.error
    argparser.error = _raise_ValueError
    try:
        argparser.parse_args(args)
    except ValueError:
        return False
    else:
        return True
    finally:
        argparser.error = old_error_method