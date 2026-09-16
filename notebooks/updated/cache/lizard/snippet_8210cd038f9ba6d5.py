def get_file_view_cls(self, filename):
    if filename is None:
        return self.default_view_class
    for pattern, cls in self.view_class_files_map:
        if pattern.match(filename):
            return cls
    return self.default_view_class