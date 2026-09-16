def static(self, uri, file_or_directory, *args, **kwargs):
    static = FutureStatic(uri, file_or_directory, args, kwargs)
    self.statics.append(static)