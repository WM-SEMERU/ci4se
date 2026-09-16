def path(self, filename):
    if not self.backend.root:
        raise OperationNotSupported(
            'Direct file access is not supported by ' + self.backend.
            __class__.__name__)
    return os.path.join(self.backend.root, filename)