def get_file(self, target, path, offset=None, length=None):
    command_block = FileSystemServiceCommandBlock()
    command_block.add_command(GetCommand(path, offset, length))
    root = _parse_command_response(self._sci_api.send_sci('file_system',
        target, command_block.get_command_string()))
    out_dict = {}
    for device in root.findall('./file_system/device'):
        device_id = device.get('id')
        error = device.find('./error')
        if error is not None:
            out_dict[device_id] = _parse_error_tree(error)
        else:
            data = GetCommand.parse_response(device.find('./commands/get_file')
                )
            out_dict[device_id] = data
    return out_dict