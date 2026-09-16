def load_libs(self, scripts_paths):
    for path in scripts_paths:
        self.run_script(_read_file(path), identifier=path)