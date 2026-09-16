def from_local_name(acs, attr, name_format):
    for aconv in acs:
        if aconv.name_format == name_format:
            return aconv.to_format(attr)
    return attr