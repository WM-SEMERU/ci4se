def join(*args, **kwargs):
    import os.path
    if _is_list(args[0]):
        return os.path.join(*args[0])
    return os.path.join(*args, **kwargs)