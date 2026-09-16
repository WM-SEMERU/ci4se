def ensure_path_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        return True
    return False