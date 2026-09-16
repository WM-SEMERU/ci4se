def check_refresh(opts, refresh=None):
    return bool(salt.utils.data.is_true(refresh) or os.path.isfile(rtag(
        opts)) and refresh is not False)