def get_project(id=None, name=None):
    content = get_project_raw(id, name)
    if content:
        return utils.format_json(content)