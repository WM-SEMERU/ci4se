def close_milestone(id, **kwargs):
    data = close_milestone_raw(id, **kwargs)
    if data:
        return utils.format_json(data)