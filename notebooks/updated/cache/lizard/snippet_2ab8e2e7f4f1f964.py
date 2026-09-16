def update_release(id, **kwargs):
    data = update_release_raw(id, **kwargs)
    if data:
        return utils.format_json(data)