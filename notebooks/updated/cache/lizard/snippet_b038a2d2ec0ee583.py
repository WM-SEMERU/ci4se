def ensure_schema(self):
    self._ensure_filename()
    if not os.path.isfile(self.filename):
        self.create_schema()