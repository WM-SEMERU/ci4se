def _iri_utf8_errors_handler(exc):
    bytes_as_ints = bytes_to_list(exc.object[exc.start:exc.end])
    replacements = [('%%%02x' % num) for num in bytes_as_ints]
    return ''.join(replacements), exc.end