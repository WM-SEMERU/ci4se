def get_config_path(filename, *search_dirs):
    paths = config_search_paths(filename, *search_dirs)
    for path in paths[::-1]:
        if os.path.exists(path):
            return path