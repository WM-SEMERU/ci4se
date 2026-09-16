def delete(self):
    fs, path = self._get_fs(create_dir=False)
    if fs.exists(path):
        fs.remove(path)
    if self.clean_dir and fs.exists('.'):
        fs.removedir('.')
    return True