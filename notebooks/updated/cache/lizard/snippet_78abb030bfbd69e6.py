def _save_stdin(self, stdin):
    self.temp_dir = TemporaryDirectory()
    file_path = os.path.join(self.temp_dir.name, 'dataset')
    try:
        with open(file_path, 'w') as f:
            for line in stdin:
                f.write(line)
    except TypeError:
        self.temp_dir.cleanup()
        raise ValueError('Could not read stdin')
    return file_path