def append_docstring(docstring, *lines):
    shallowest = get_minimum_indent(docstring)
    appender = []
    for line in lines:
        appender.append('\n')
        if line.strip():
            appender.append(shallowest)
            appender.append(line)
    return docstring + ''.join(appender)