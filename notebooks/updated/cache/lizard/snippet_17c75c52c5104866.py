def update_build_configuration(id, **kwargs):
    data = update_build_configuration_raw(id, **kwargs)
    if data:
        return utils.format_json(data)