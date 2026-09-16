def sanitize(self):
    if not self.args.hide_file_names:
        return self
    if self.entity is None:
        return self
    if self.type != 'file':
        return self
    if self.should_obfuscate_filename():
        self._sanitize_metadata()
        extension = u(os.path.splitext(self.entity)[1])
        self.entity = u('HIDDEN{0}').format(extension)
    elif self.should_obfuscate_project():
        self._sanitize_metadata()
    return self