def filter_basis_sets(substr=None, family=None, role=None, data_dir=None):
    data_dir = fix_data_dir(data_dir)
    metadata = get_metadata(data_dir)
    if family:
        family = family.lower()
        if not family in get_families(data_dir):
            raise RuntimeError("Family '{}' is not a valid family".format(
                family))
        metadata = {k: v for k, v in metadata.items() if v['family'] == family}
    if role:
        role = role.lower()
        if not role in get_roles():
            raise RuntimeError("Role '{}' is not a valid role".format(role))
        metadata = {k: v for k, v in metadata.items() if v['role'] == role}
    if substr:
        substr = substr.lower()
        metadata = {k: v for k, v in metadata.items() if substr in k or 
            substr in v['display_name']}
    return metadata