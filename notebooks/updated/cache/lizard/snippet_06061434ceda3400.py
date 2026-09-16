def extract_function_argument(text, f_name, f_argn, f_argt=asttypes.String):
    tree = parse(text)
    return list(filter_function_argument(tree, f_name, f_argn, f_argt))