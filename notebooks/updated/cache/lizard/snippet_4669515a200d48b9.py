def add_srec_file(self, filename, overwrite=False):
    with open(filename, 'r') as fin:
        self.add_srec(fin.read(), overwrite)