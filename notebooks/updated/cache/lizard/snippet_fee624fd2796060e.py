def get_uploadflags(self, location):
    uploadflags = []
    server = self.defaults.servers[location]
    if self.sign:
        uploadflags.append('--sign')
    elif server.sign is not None:
        if server.sign:
            uploadflags.append('--sign')
    elif self.defaults.sign:
        uploadflags.append('--sign')
    if self.identity:
        if '--sign' not in uploadflags:
            uploadflags.append('--sign')
        uploadflags.append('--identity="%s"' % self.identity)
    elif '--sign' in uploadflags:
        if server.identity is not None:
            if server.identity:
                uploadflags.append('--identity="%s"' % server.identity)
        elif self.defaults.identity:
            uploadflags.append('--identity="%s"' % self.defaults.identity)
    return uploadflags