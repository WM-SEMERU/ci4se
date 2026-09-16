def parse_extension_arg(arg, arg_dict):
    match = re.match('^(([^\\d\\W]\\w*)(\\.[^\\d\\W]\\w*)*)=(.*)$', arg)
    if match is None:
        raise ValueError(
            "invalid extension argument '%s', must be in key=value form" % arg)
    name = match.group(1)
    value = match.group(4)
    arg_dict[name] = value