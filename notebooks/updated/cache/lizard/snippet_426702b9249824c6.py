def process_command_response(self, command, response):
    if response.startswith(b'Unknown command.'):
        raise UnknownCommandError(command)
    if response == b'Permission denied.\n':
        raise PermissionError(command)
    if response == b'No such backend.\n':
        raise UnknownServerError(command)
    response = response.decode()
    return response.rstrip('\n')