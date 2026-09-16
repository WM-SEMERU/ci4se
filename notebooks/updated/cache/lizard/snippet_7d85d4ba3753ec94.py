def include(self, path):
    for extension in IGNORE_EXTENSIONS:
        if path.endswith(extension):
            return False
    parts = path.split(os.path.sep)
    for part in parts:
        if part in self.ignore_dirs:
            return False
    return True