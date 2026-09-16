def resource_present(name, resource_id, resource_type, resource_options=
    None, cibname=None):
    return _item_present(name=name, item='resource', item_id=resource_id,
        item_type=resource_type, extra_args=resource_options, cibname=cibname)