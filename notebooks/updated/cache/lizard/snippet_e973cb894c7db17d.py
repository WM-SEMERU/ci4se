def new_transient(self, ext=''):
    name = random_name(self.transient_length) + ext
    return TransientFile(self.transient_root, name, self)