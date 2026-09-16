def _jq_format(code):
    code = code.replace('\\', '\\\\').replace('\t', '\\t').replace('\n', '\\n')
    code = code.replace('"', '\\"').replace("'", "\\'")
    code = code.replace('\x0b', '\\v').replace('\x07', '\\a').replace('\x0c',
        '\\f')
    code = code.replace('\x08', '\\b').replace('\\u', '\\u').replace('\r',
        '\\r')
    return code