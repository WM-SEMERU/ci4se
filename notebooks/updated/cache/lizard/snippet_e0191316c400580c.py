def add_folder(self, path, depth=None, source_type=DefaultSourceType):
    self.add_source(FolderSource(path, depth, **source_type))
    return self