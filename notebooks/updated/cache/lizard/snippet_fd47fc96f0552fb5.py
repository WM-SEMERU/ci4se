def get_fp_version(self):
    command = const.CMD_OPTIONS_RRQ
    command_string = b'~ZKFPVersion\x00'
    response_size = 1024
    cmd_response = self.__send_command(command, command_string, response_size)
    if cmd_response.get('status'):
        response = self.__data.split(b'=', 1)[-1].split(b'\x00')[0]
        response = response.replace(b'=', b'')
        return safe_cast(response, int, 0) if response else 0
    else:
        raise ZKErrorResponse("can't read fingerprint version")