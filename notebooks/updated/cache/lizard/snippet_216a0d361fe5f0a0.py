def _compat_name(new_name, compat_name=None):
    if compat_name is not None:
        assert 'slave' in compat_name.lower()
        assert new_name == '' or 'worker' in new_name.lower(), new_name
        return compat_name
    compat_replacements = {'worker': 'slave', 'Worker': 'Slave'}
    compat_name = new_name
    assert 'slave' not in compat_name.lower()
    assert 'worker' in compat_name.lower()
    for new_word, old_word in compat_replacements.items():
        compat_name = compat_name.replace(new_word, old_word)
    assert compat_name != new_name
    assert 'slave' in compat_name.lower()
    assert 'worker' not in compat_name.lower()
    return compat_name