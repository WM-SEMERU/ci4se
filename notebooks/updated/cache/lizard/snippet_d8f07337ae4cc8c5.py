def from_file(self, fname, comment_lead=['c'], compressed_with='use_ext'):
    with FileObject(fname, mode='r', compression=compressed_with) as fobj:
        self.from_fp(fobj.fp, comment_lead)