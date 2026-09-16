def is_incomplete_option(all_args, cmd_param):
    if not isinstance(cmd_param, Option):
        return False
    if cmd_param.is_flag:
        return False
    last_option = None
    for index, arg_str in enumerate(reversed([arg for arg in all_args if 
        arg != WORDBREAK])):
        if index + 1 > cmd_param.nargs:
            break
        if start_of_option(arg_str):
            last_option = arg_str
    return True if last_option and last_option in cmd_param.opts else False