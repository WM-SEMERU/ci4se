def element_isaligned(self, other):
    assert isinstance(other, Matrix
        ), 'Matrix.isaligned(): other argument must be type Matrix, not: ' + str(
        type(other))
    if self.row_names == other.row_names and self.col_names == other.col_names:
        return True
    else:
        return False