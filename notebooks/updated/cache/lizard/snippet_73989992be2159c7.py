def slurpLines(file, expand=False):
    r
    file = _normalizeToFile(file, 'r', expand)
    try:
        return file.readlines()
    finally:
        file.close()