def _parse(fileobj):
    fileobj.seek(0)
    try:
        part = fileobj.read(2)
    except UnicodeDecodeError:
        part = ''
    if part == '#!':
        shebang = shlex.split(fileobj.readline().strip())
        if platform.system() == 'Windows' and len(shebang
            ) and os.path.basename(shebang[0]) == 'env':
            return shebang[1:]
        return shebang
    return []