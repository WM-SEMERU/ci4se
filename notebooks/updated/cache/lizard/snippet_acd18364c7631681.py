def build_options(self):
    if self.version.build_metadata:
        return set(self.version.build_metadata.split('.'))
    else:
        return set()