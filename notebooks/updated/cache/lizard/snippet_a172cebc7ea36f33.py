def remove(self, path, recursive=True, skip_trash=False):
    return list(self.get_bite().delete(self.list_path(path), recurse=recursive)
        )