def find_commands(cls):
    cmds = []
    for subclass in cls.__subclasses__():
        cmds.append(subclass)
        cmds.extend(find_commands(subclass))
    return cmds