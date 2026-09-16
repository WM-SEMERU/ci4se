def make_diagonal_povm(pi_basis, confusion_rate_matrix):
    confusion_rate_matrix = np.asarray(confusion_rate_matrix)
    if not np.allclose(confusion_rate_matrix.sum(axis=0), np.ones(
        confusion_rate_matrix.shape[1])):
        raise CRMUnnormalizedError('Unnormalized confusion matrix:\n{}'.
            format(confusion_rate_matrix))
    if not (confusion_rate_matrix >= 0).all() or not (confusion_rate_matrix <=
        1).all():
        raise CRMValueError('Confusion matrix must have values in [0, 1]:\n{}'
            .format(confusion_rate_matrix))
    ops = [sum((pi_j * pjk for pi_j, pjk in izip(pi_basis.ops, pjs)), 0) for
        pjs in confusion_rate_matrix]
    return DiagonalPOVM(pi_basis=pi_basis, confusion_rate_matrix=
        confusion_rate_matrix, ops=ops)