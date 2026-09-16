def import_path(self):
    return os.path.join(self.remote_root, self.pkg
        ) if self.pkg else self.remote_root