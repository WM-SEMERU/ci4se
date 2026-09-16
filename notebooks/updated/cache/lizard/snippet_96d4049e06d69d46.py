def _ParseShellItemPathSegment(self, shell_item):
    path_segment = None
    if isinstance(shell_item, pyfwsi.root_folder):
        description = shell_folder_ids.DESCRIPTIONS.get(shell_item.
            shell_folder_identifier, None)
        if description:
            path_segment = description
        else:
            path_segment = '{{{0:s}}}'.format(shell_item.
                shell_folder_identifier)
        path_segment = '<{0:s}>'.format(path_segment)
    elif isinstance(shell_item, pyfwsi.volume):
        if shell_item.name:
            path_segment = shell_item.name
        elif shell_item.identifier:
            path_segment = '{{{0:s}}}'.format(shell_item.identifier)
    elif isinstance(shell_item, pyfwsi.file_entry):
        long_name = ''
        for extension_block in shell_item.extension_blocks:
            if isinstance(extension_block, pyfwsi.file_entry_extension):
                long_name = extension_block.long_name
        if long_name:
            path_segment = long_name
        elif shell_item.name:
            path_segment = shell_item.name
    elif isinstance(shell_item, pyfwsi.network_location):
        if shell_item.location:
            path_segment = shell_item.location
    if path_segment is None and shell_item.class_type == 0:
        pass
    if path_segment is None:
        path_segment = '<UNKNOWN: 0x{0:02x}>'.format(shell_item.class_type)
    return path_segment