def get_command(arguments):
    return [k for k, v in arguments.items() if not k.startswith('-') and v is
        True][0]