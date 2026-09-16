def instance_contains(container, item):
    return item in (member for _, member in inspect.getmembers(container))