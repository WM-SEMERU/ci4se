def split_by_line(content):
    stripped = content.strip()
    if not stripped:
        return []
    if '\r\n' in stripped:
        return _strip_all(stripped.split('\r\n'))
    if '\n' in stripped:
        return _strip_all(stripped.split('\n'))
    return _strip_all([stripped])