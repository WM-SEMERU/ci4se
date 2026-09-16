def _is_updated(old_conf, new_conf):
    changed = {}
    new_conf = _json_to_unicode(salt.utils.json.loads(salt.utils.json.dumps
        (new_conf, ensure_ascii=False)))
    old_conf = salt.utils.json.loads(salt.utils.json.dumps(old_conf,
        ensure_ascii=False))
    for key, value in old_conf.items():
        oldval = six.text_type(value).lower()
        if key in new_conf:
            newval = six.text_type(new_conf[key]).lower()
        if oldval == 'null' or oldval == 'none':
            oldval = ''
        if key in new_conf and newval != oldval:
            changed[key] = {'old': oldval, 'new': newval}
    return changed