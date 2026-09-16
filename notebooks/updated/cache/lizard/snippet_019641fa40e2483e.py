def parse_gdb_version(line):
    r
    if line.startswith('~"') and line.endswith('\\n"'):
        version = line[2:-3].rsplit(' ', 1)
        if len(version) == 2:
            version = ''.join(takewhile(lambda x: x.isdigit() or x == '.',
                version[1].lstrip('(')))
            return version.strip('.')
    return ''