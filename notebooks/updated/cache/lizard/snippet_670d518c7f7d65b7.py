def read(self, file_or_path):
    if file_or_path in self._cached_templates:
        return self._cached_templates[file_or_path]
    if is_filelike(file_or_path):
        template = file_or_path.read()
        dirname = None
    else:
        with open(file_or_path, 'r') as f:
            template = f.read()
        dirname = os.path.dirname(file_or_path)
    template = self._engine(template, dirname=dirname, tolerant=self._tolerant)
    self._cached_templates[file_or_path] = template
    return template