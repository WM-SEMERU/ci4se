def write_packed(self, outfile, rows):
    return self.write_passes(outfile, rows, packed=True)