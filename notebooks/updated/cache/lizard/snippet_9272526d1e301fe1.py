def _get_temp_file_location():
    from .._connect import main as _glconnect
    unity = _glconnect.get_unity()
    cache_dir = _convert_slashes(unity.get_current_cache_file_location())
    if not _os.path.exists(cache_dir):
        _os.makedirs(cache_dir)
    return cache_dir