def generate_minion_id():
    try:
        ret = salt.utils.stringutils.to_unicode(_generate_minion_id().first())
    except TypeError:
        ret = None
    return ret or 'localhost'