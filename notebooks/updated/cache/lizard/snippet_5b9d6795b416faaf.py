def remove_file(path, remove=os.remove, exists=os.path.exists):
    try:
        remove(path)
    except OSError:
        if exists(path):
            raise