def find_file_paths(self):
    paths = []
    for root, dirs, files in os.walk(self.directory, topdown=True):
        rel_path = os.path.relpath(root, self.directory)
        for f in files:
            if rel_path == '.':
                path = f, os.path.join(root, f)
            else:
                path = os.path.join(rel_path, f), os.path.join(root, f)
            paths.append(path)
    return paths