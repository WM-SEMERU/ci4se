def dir_modtime(dpath):
    return max(os.path.getmtime(d) for d, _, _ in os.walk(dpath))