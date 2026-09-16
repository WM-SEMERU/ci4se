def write_file(self, filename=None, buffer=None, fileobj=None):
    closefile = True
    if buffer:
        self.filename = None
        self.file = buffer
        closefile = False
    elif filename:
        self.filename = filename
        self.file = GzipFile(filename, 'wb')
    elif fileobj:
        self.filename = None
        self.file = GzipFile(fileobj=fileobj, mode='wb')
    elif self.filename:
        self.file = GzipFile(self.filename, 'wb')
    elif not self.file:
        raise ValueError(
            'NBTFile.write_file(): Need to specify either a filename or a file object'
            )
    TAG_Byte(self.id)._render_buffer(self.file)
    TAG_String(self.name)._render_buffer(self.file)
    self._render_buffer(self.file)
    try:
        self.file.flush()
    except (AttributeError, IOError):
        pass
    if closefile:
        try:
            self.file.close()
        except (AttributeError, IOError):
            pass