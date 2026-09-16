def find_version_by_regex(file_source, version_token='__version__'):
    if not file_source:
        return None
    version_match = re.search('^' + version_token +
        ' = [\'\\"]([^\'\\"]*)[\'\\"]', file_source, re.M)
    if version_match:
        candidate = version_match.group(1)
        if candidate == '' or candidate == '.':
            return None
        return candidate
    return None