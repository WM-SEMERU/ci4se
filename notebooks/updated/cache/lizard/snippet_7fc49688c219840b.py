def safe_filename(filename, replacement='_'):
    if not isinstance(filename, str):
        raise TypeError('filename must be a string')
    if regex.path.linux.filename.search(filename):
        return filename
    safe_name = ''
    for char in filename:
        safe_name += char if regex.path.linux.filename.search(char
            ) else replacement
    return safe_name