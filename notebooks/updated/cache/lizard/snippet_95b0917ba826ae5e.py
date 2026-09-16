def find_command_class(possible_command_names):
    for command_name in possible_command_names:
        if hasattr(ALL_COMMANDS_MODULE, command_name):
            command_module = getattr(ALL_COMMANDS_MODULE, command_name)
            command_class_hierarchy = getmembers(command_module, isclass)
            command_class_tuple = list(filter(_not_base_class,
                command_class_hierarchy))[0]
            return command_class_tuple[1]
    return None