def _escape_xref(xref_match):
    xref = xref_match.group()
    xref = xref.replace('/', '%2F')
    xref = xref.replace('?', '%3F')
    xref = xref.replace('#', '%23')
    return xref