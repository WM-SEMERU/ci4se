def full_name(self):
    names = [self._builder.name]
    if self._builder.builder_config:
        names.append(self._builder.builder_config.name)
    names.append(str(self.version))
    return posixpath.join(*names)