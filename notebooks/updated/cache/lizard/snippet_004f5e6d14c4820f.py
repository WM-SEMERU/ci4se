def __print_command_help(self, session, namespace, cmd_name):
    args, doc = self.__extract_help(self._commands[namespace][cmd_name])
    if args:
        session.write_line('- {0} {1}', cmd_name, args)
    else:
        session.write_line('- {0}', cmd_name)
    session.write_line('\t\t{0}', doc)