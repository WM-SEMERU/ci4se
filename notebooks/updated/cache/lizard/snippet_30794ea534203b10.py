def get_dual(self, constraint, ymat=None):
    if not isinstance(constraint, Expr):
        raise Exception('Not a monomial or polynomial!')
    elif self.status == 'unsolved' and ymat is None:
        raise Exception('SDP relaxation is not solved yet!')
    elif ymat is None:
        ymat = self.y_mat
    index = self._constraint_to_block_index.get(constraint)
    if index is None:
        raise Exception('Constraint is not in the dual!')
    if len(index) == 2:
        return ymat[index[0]], self.y_mat[index[1]]
    else:
        return ymat[index[0]]