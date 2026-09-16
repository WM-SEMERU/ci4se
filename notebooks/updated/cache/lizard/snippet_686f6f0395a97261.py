def isPythonFile(filename):
    if filename.endswith('.py'):
        return True
    if filename.endswith('~'):
        return False
    max_bytes = 128
    try:
        with open(filename, 'rb') as f:
            text = f.read(max_bytes)
            if not text:
                return False
    except IOError:
        return False
    first_line = text.splitlines()[0]
    return PYTHON_SHEBANG_REGEX.match(first_line)