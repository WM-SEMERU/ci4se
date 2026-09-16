def name_from_path(self):
    name = os.path.splitext(os.path.basename(self.path))[0]
    if name == 'catalog':
        name = os.path.basename(os.path.dirname(self.path))
    return name.replace('.', '_')