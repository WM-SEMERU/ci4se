def defaultExtension(self):
    result = self.EXTERNAL_TYPES[self.typ]
    if not self.fileExtensions:
        return result
    if result in self.fileExtensions:
        return result
    return self.fileExtensions[0]