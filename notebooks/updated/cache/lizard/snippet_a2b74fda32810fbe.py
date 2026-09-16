def folders(self):
    for directory in self.directory:
        for path in os.listdir(directory):
            full_path = os.path.join(directory, path)
            if os.path.isdir(full_path):
                if not path.startswith('.'):
                    self.filepaths.append(full_path)
    return self._get_filepaths()