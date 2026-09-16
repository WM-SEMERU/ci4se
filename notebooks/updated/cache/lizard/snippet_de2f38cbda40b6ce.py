def get_storage_path(filename):
    directory = os.path.join(STORAGE_DIRECTORY, filename[0], filename[1])
    if not os.path.exists(directory):
        os.makedirs(directory)
    return os.path.join(directory, filename)