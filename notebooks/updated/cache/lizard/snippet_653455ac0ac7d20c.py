def x10_command_type(command):
    command_type = X10CommandType.DIRECT
    if command in [X10_COMMAND_ALL_UNITS_OFF, X10_COMMAND_ALL_LIGHTS_ON,
        X10_COMMAND_ALL_LIGHTS_OFF]:
        command_type = X10CommandType.BROADCAST
    return command_type