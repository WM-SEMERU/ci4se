def strip_comments(text):
    regex = '\\s*(#|\\/{2}).*$'
    regex_inline = (
        '(:?(?:\\s)*([A-Za-z\\d\\.{}]*)|((?<=\\").*\\"),?)(?:\\s)*(((#|(\\/{2})).*)|)$'
        )
    lines = text.split('\n')
    for index, line in enumerate(lines):
        if re.search(regex, line):
            if re.search('^' + regex, line, re.IGNORECASE):
                lines[index] = ''
            elif re.search(regex_inline, line):
                lines[index] = re.sub(regex_inline, '\\1', line)
    return '\n'.join(lines)