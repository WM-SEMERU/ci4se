def get_file(self, name):
    files = self.get_output_files()
    for f in files:
        if f.get_name() == name:
            return f
    return None