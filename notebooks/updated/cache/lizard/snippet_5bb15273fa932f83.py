def update_build_configuration_set(id, **kwargs):
    data = update_build_configuration_set_raw(id, **kwargs)
    if data:
        return utils.format_json(data)