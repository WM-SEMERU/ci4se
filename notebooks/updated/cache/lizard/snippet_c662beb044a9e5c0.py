def sub_files(path, invisible=False):
    files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(
        path, x))]
    if not invisible:
        files = [x for x in files if not x.startswith('.')]
    return files