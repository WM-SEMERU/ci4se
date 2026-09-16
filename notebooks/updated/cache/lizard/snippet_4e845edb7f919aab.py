def logical_lines(lines):
    if isinstance(lines, string_types):
        lines = StringIO(lines)
    buf = []
    for line in lines:
        if buf and not line.startswith(' '):
            chunk = ''.join(buf).strip()
            if chunk:
                yield chunk
            buf[:] = []
        buf.append(line)
    chunk = ''.join(buf).strip()
    if chunk:
        yield chunk