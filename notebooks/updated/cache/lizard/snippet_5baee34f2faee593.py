def delete(self, key):
    path = self.object_path(key)
    if os.path.exists(path):
        os.remove(path)