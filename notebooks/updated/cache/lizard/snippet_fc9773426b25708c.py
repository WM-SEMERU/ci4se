def object_ns(self):
    return Namespace(subject=self.object_, object_=None, prefix=self.prefix,
        qualifier=self.qualifier, version=self.version)