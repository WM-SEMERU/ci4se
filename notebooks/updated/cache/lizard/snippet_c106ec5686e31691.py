def add_copy_spec_limit_scl(self, scl, copyspec, **kwargs):
    self.add_copy_spec_limit(self.convert_copyspec_scl(scl, copyspec), **kwargs
        )