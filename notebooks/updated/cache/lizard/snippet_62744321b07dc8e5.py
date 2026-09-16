def load_file(self, filename):
    filename = os.path.abspath(filename)
    with open(filename) as f:
        self.load_dict(yaml.load(f))
    self._loaded_files.append(filename)