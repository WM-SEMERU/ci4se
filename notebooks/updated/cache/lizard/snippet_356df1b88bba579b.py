def _write_wrapped(self, line, sep=' ', indent='', width=78):
    words = line.split(sep)
    lines = []
    line = ''
    buf = []
    while len(words):
        buf.append(words.pop(0))
        line = sep.join(buf)
        if len(line) > width:
            words.insert(0, buf.pop())
            lines.append(sep.join(buf))
            buf = []
            line = ''
    if line:
        lines.append(line)
    result = lines.pop(0)
    if len(lines):
        eol = ''
        if sep == ' ':
            eol = '\\s'
        for item in lines:
            result += eol + '\n' + indent + '^ ' + item
    return result