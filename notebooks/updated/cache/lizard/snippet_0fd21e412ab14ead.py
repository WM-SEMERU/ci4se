def get_child(self):
    path_parts = self.remote_path.split(os.sep)
    return self._get_child_recurse(path_parts, self.node)