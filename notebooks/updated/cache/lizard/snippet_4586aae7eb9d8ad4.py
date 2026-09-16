def default_child_path(path):
    try:
        child_path = default_child_path(current_app.config[
            'DEFAULT_CHILDREN'][path])
    except KeyError:
        child_path = path
    return child_path