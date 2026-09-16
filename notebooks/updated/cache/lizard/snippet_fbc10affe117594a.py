def function_path(func):
    if getattr(func, 'func_code', None):
        return func.__code__.co_filename.replace('\\', '/')
    else:
        return func.__code__.co_filename.replace('\\', '/')