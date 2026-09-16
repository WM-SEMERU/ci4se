def parse_arg_list(param_start):
    values = [arg[len(param_start):] for arg in sys.argv if arg.startswith(
        param_start)]
    otherArgs = [arg for arg in sys.argv if not arg.startswith(param_start)]
    sys.argv = otherArgs
    return values