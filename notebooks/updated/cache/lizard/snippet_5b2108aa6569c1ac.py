def _rm_get_names_from_header(parts):
    assert parts[8] == 'C' and len(parts) == 15 or len(parts) == 14
    return (parts[4], parts[8]) if len(parts) == 14 else (parts[4], parts[9])