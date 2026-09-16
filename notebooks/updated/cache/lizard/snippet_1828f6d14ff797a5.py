def save_model(self, fname, include_unsigned_edges=False):
    sif_str = self.print_model(include_unsigned_edges)
    with open(fname, 'wb') as fh:
        fh.write(sif_str.encode('utf-8'))