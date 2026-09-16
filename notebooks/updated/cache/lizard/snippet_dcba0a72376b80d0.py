def _is_gwf(file_path):
    try:
        with open(file_path, 'rb') as f:
            if f.read(4) == b'IGWD':
                return True
    except IOError:
        pass
    return False