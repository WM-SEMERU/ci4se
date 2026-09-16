def ensure_path_exists(dir_path):
    if not os.path.exists(dir_path):
        mkdir(dir_path)
        return True
    return False