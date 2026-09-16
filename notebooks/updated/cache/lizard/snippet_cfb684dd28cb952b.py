def _parse_mods(mods):
    if isinstance(mods, six.string_types):
        mods = [item.strip() for item in mods.split(',') if item.strip()]
    return mods