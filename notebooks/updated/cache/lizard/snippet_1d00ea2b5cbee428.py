def read_file(self, path):
    self.assert_valid_path(path)
    with open(path, 'rb') as file:
        contents = file.read().decode('UTF-8')
    return contents