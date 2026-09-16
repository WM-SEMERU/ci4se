def select_from(self, parent_path):
    path_cls = type(parent_path)
    is_dir = path_cls.is_dir
    exists = path_cls.exists
    listdir = parent_path._accessor.listdir
    return self._select_from(parent_path, is_dir, exists, listdir)