def _set_key(log_prefix, result_dict, key, value, desc='parameter'):
    if key in result_dict:
        LOG.warn('%s: Duplicate value for %s %r' % (log_prefix, desc, key))
    if len(value) <= 2 or value[0] not in ('"', "'") or value[0] != value[-1]:
        LOG.warn('%s: Invalid value %r for %s %r' % (log_prefix, value,
            desc, key))
        return
    result_dict[key] = value[1:-1]