def get_size(fileobj):
    old_pos = fileobj.tell()
    try:
        fileobj.seek(0, 2)
        return fileobj.tell()
    finally:
        fileobj.seek(old_pos, 0)