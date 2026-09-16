def watchable(value):
    check = issubclass if inspect.isclass(value) else isinstance
    return check(value, Watchable)