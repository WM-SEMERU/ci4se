def from_string(string, mime=False, filename=None):
    head, foot = _string_details(string)
    ext = ext_from_filename(filename) if filename else None
    return _magic(head, foot, mime, ext)