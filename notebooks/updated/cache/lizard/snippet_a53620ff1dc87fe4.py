def comment_out_magics(source):
    filtered = []
    for line in source.splitlines():
        if line.strip().startswith('%'):
            filtered.append('# ' + line)
        else:
            filtered.append(line)
    return '\n'.join(filtered)