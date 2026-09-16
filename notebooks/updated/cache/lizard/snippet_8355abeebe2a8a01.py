def parse_multipart_headers(iterable):
    result = []
    for line in iterable:
        line = to_native(line)
        line, line_terminated = _line_parse(line)
        if not line_terminated:
            raise ValueError('unexpected end of line in multipart header')
        if not line:
            break
        elif line[0] in ' \t' and result:
            key, value = result[-1]
            result[-1] = key, value + '\n ' + line[1:]
        else:
            parts = line.split(':', 1)
            if len(parts) == 2:
                result.append((parts[0].strip(), parts[1].strip()))
    return Headers(result)