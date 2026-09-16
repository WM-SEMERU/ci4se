def get_file_str(path, saltenv='base'):
    fn_ = cache_file(path, saltenv)
    if isinstance(fn_, six.string_types):
        try:
            with salt.utils.files.fopen(fn_, 'r') as fp_:
                return fp_.read()
        except IOError:
            return False
    return fn_