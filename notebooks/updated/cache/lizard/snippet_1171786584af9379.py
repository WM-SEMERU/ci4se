def _shape2pys(self):
    shape_line = '\t'.join(map(unicode, self.code_array.shape)) + '\n'
    self.pys_file.write(shape_line)