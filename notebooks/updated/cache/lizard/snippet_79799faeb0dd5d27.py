def make_regex(separator):
    return re.compile('(?:' + re.escape(separator) + ')?((?:[^' + re.escape
        (separator) + '\\\\]|\\\\.)+)')