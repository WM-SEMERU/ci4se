def copy_current_file_offset():
    start, end = sark.get_selection()
    try:
        file_offset = sark.core.get_fileregion_offset(start)
        clipboard.copy('0x{:08X}'.format(file_offset))
    except sark.exceptions.NoFileOffset:
        message(
            'The current address cannot be mapped to a valid offset of the input file.'
            )