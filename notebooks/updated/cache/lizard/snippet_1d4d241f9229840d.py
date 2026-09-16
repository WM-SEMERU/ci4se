def file_remove(self, path, filename):
    if os.path.isfile(path + filename):
        os.remove(path + filename)