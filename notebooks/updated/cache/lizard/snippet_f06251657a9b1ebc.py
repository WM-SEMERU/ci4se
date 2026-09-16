def strip_required_prefix(string, prefix):
    if string.startswith(prefix):
        return string[len(prefix):]
    raise AssertionError('String starts with %r, not %r' % (string[:len(
        prefix)], prefix))