def __update_cleanup_paths(new_path):
    cleanup_dirs = settings.CFG['cleanup_paths'].value
    cleanup_dirs = set(cleanup_dirs)
    cleanup_dirs.add(new_path)
    cleanup_dirs = list(cleanup_dirs)
    settings.CFG['cleanup_paths'] = cleanup_dirs