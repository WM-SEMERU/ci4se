def get_file_path(filename, local=True, relative_to_module=None, my_dir=my_dir
    ):
    if relative_to_module is not None:
        my_dir = os.path.dirname(relative_to_module.__file__)
    user_path = result = filename
    if local:
        user_path = os.path.expanduser(filename)
        result = os.path.abspath(user_path)
        if os.path.exists(result):
            return result
    result = os.path.join(my_dir, filename)
    assert os.path.exists(result), 'no such file ' + repr((filename, result,
        user_path))
    return result