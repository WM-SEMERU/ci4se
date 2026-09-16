def jkeys(jfile, key_path=None, in_memory=True, ignore_prefix=('.', '_')):
    key_path = [] if key_path is None else key_path

    def eval_file(file_obj):
        if not in_memory:
            return _get_keys_ijson(file_obj, key_path)
        else:
            return _get_keys(file_obj, key_path)
    if isinstance(jfile, basestring):
        if not os.path.exists(jfile):
            raise IOError('jfile does not exist: {}'.format(jfile))
        if os.path.isdir(jfile):
            jpath = pathlib.Path(jfile)
            return _get_keys_folder(jpath, key_path, in_memory, ignore_prefix)
        else:
            with open(jfile, 'r') as file_obj:
                return eval_file(file_obj)
    elif hasattr(jfile, 'read'):
        return eval_file(jfile)
    elif hasattr(jfile, 'iterdir'):
        if jfile.is_file():
            with jfile.open('r') as file_obj:
                return eval_file(file_obj)
        else:
            return _get_keys_folder(jfile, key_path, in_memory, ignore_prefix)
    else:
        raise ValueError(
            'jfile should be a str, file_like or path_like object: {}'.
            format(jfile))