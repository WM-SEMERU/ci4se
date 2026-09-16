def copy_contents(self, fileinstance, progress_callback=None, chunk_size=
    None, **kwargs):
    if not fileinstance.readable:
        raise ValueError('Source file instance is not readable.')
    if not self.size == 0:
        raise ValueError('File instance has data.')
    self.set_uri(*self.storage(**kwargs).copy(fileinstance.storage(**kwargs
        ), chunk_size=chunk_size, progress_callback=progress_callback))