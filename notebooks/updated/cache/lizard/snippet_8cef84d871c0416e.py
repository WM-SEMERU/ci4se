def add_prefix_and_suffix(specified_name, type, property_set):
    property_set = b2.util.jam_to_value_maybe(property_set)
    suffix = ''
    if type:
        suffix = b2.build.type.generated_target_suffix(type, property_set)
    if get_grist(suffix):
        suffix = ungrist(suffix)
    elif suffix:
        suffix = '.' + suffix
    prefix = ''
    if type:
        prefix = b2.build.type.generated_target_prefix(type, property_set)
    if specified_name.startswith(prefix):
        prefix = ''
    if not prefix:
        prefix = ''
    if not suffix:
        suffix = ''
    return prefix + specified_name + suffix