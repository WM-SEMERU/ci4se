def save(self, file_or_wfs, filename=None, prefix=None, overwrite=None):
    if not filename and isinstance(file_or_wfs, FileStorage):
        filename = lower_extension(secure_filename(file_or_wfs.filename))
    if not filename:
        raise ValueError('filename is required')
    if not self.file_allowed(file_or_wfs, filename):
        raise UnauthorizedFileType()
    if prefix:
        filename = '/'.join((prefix() if callable(prefix) else prefix,
            filename))
    if self.upload_to:
        upload_to = self.upload_to() if callable(self.upload_to
            ) else self.upload_to
        filename = '/'.join((upload_to, filename))
    overwrite = self.overwrite if overwrite is None else overwrite
    if not overwrite and self.exists(filename):
        raise FileExists(filename)
    self.backend.save(file_or_wfs, filename)
    return filename