def _collect_valid_settings(meta, clsdict):
    enum_members = clsdict['__members__']
    valid_settings = []
    for member in enum_members:
        valid_settings.extend(member.valid_settings)
    clsdict['_valid_settings'] = valid_settings