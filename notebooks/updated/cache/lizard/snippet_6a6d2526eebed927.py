def remove_blank_lines(source):
    io_obj = io.StringIO(source)
    source = [a for a in io_obj.readlines() if a.strip()]
    return ''.join(source)