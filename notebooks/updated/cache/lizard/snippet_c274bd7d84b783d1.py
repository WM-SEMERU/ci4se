def delete_file(self, target, path):
    command_block = FileSystemServiceCommandBlock()
    command_block.add_command(DeleteCommand(path))
    root = _parse_command_response(self._sci_api.send_sci('file_system',
        target, command_block.get_command_string()))
    out_dict = {}
    for device in root.findall('./file_system/device'):
        device_id = device.get('id')
        error = device.find('./error')
        if error is not None:
            out_dict[device_id] = _parse_error_tree(error)
        else:
            out_dict[device_id] = DeleteCommand.parse_response(device.find(
                './commands/rm'))
    return out_dict