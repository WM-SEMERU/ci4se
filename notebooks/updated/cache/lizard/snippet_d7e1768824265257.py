def _get_shortcut_string(shortcut):
    if shortcut is None:
        return ''
    if isinstance(shortcut, (tuple, list)):
        return ', '.join([_get_shortcut_string(s) for s in shortcut])
    if isinstance(shortcut, string_types):
        if hasattr(QKeySequence, shortcut):
            shortcut = QKeySequence(getattr(QKeySequence, shortcut))
        else:
            return shortcut.lower()
    assert isinstance(shortcut, QKeySequence)
    s = shortcut.toString() or ''
    return str(s).lower()