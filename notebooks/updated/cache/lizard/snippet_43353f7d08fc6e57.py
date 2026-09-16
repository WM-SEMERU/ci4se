def send_command_return(self, obj, command, *arguments):
    index_command = obj._build_index_command(command, *arguments)
    return obj._extract_return(command, self.chassis_list[obj.chassis].
        sendQuery(index_command))