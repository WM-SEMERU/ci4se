def key_rollover(kb):
    key_spec = []
    for key in kb.get():
        _spec = {'type': key.kty, 'use': [key.use]}
        if key.kty == 'EC':
            _spec['crv'] = key.crv
        key_spec.append(_spec)
    diff = {'del': kb.get()}
    _kb = build_key_bundle(key_spec)
    diff['add'] = _kb.keys()
    update_key_bundle(kb, diff)
    return kb