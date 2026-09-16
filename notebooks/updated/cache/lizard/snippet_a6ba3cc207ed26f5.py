def store(self, transient_file, persistent_file):
    dirname = os.path.dirname(persistent_file.path)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    os.rename(transient_file.path, persistent_file.path)
    return persistent_file