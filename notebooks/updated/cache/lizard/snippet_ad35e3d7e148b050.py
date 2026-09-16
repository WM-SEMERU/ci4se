def _find_combo_match(path):
    key_str = _form_key_str(path)
    if not key_str:
        return None
    if not msettings['JOINED'].has_key(key_str):
        return None
    else:
        return key_str