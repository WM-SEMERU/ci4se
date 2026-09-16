def fetch_and_convert_dataset(source_files, target_filename):
    if not isinstance(target_filename, six.string_types) and not callable(
        target_filename):
        raise TypeError(
            'target_filename must either be a string or be callable (it is a {})'
            .format(type(target_filename)))
    for src in source_files:
        if not isinstance(src, AbstractSourceFile):
            raise TypeError(
                'source_files should contain`AbstractSourceFile` instances, not {}'
                .format(type(src)))

    def decorate_fetcher(convert_function):

        def fetch(**kwargs):
            target_fn = path_string(target_filename)
            target_path = config.get_data_path(target_fn)
            if not os.path.exists(target_path):
                source_paths = []
                for src in source_files:
                    p = src.acquire(**kwargs)
                    if p is not None:
                        if p in source_paths:
                            raise ValueError('Duplicate source file {}'.
                                format(p))
                        source_paths.append(p)
                    else:
                        print('Failed to acquire {}'.format(src))
                        return None
                converted_path = convert_function(source_paths, target_path)
                if converted_path is not None:
                    for src in source_files:
                        src.clean_up()
                return converted_path
            else:
                return target_path
        fetch.__name__ = convert_function.__name__
        return fetch
    return decorate_fetcher