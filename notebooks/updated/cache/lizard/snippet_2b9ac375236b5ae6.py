def write_dfile(self):
    f_in = self.tempfiles.get_tempfile(prefix='bmds-', suffix='.(d)')
    with open(f_in, 'w') as f:
        f.write(self.as_dfile())
    return f_in