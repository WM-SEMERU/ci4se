def clear_attendance(self):
    command = const.CMD_CLEAR_ATTLOG
    cmd_response = self.__send_command(command)
    if cmd_response.get('status'):
        return True
    else:
        raise ZKErrorResponse("Can't clear response")