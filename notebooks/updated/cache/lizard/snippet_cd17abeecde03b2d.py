def _escape_regexp(s):
    return str(s).replace('|', '\\|').replace('.', '\\.').replace('*', '.*'
        ).replace('+', '\\+').replace('(', '\\(').replace(')', '\\)').replace(
        '$', '\\$')