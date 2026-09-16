def load_child_node(self, key):
    index = self.get_child_index(key)
    if key is None:
        return EmptyNode(None)
    else:
        path = os.path.join(self.get_value(), key)
        if index < self.dir_count:
            return DirectoryNode(path, self.display, parent=self)
        else:
            path = os.path.join(self.get_value(), key)
            return FileNode(path, self.display, parent=self)