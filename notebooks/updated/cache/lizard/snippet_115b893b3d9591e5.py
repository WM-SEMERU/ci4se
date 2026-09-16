def register_command(parent_command, name):

    def wrapper(func):
        c = command(name)(func)
        parent_command.add_subcommand(c)
    return wrapper