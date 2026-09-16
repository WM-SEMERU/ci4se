def scipy_solve_symm_block_tridiag(H_diag, H_upper_diag, v, ab=None):
    from scipy.linalg import solveh_banded
    ab = convert_block_tridiag_to_banded(H_diag, H_upper_diag
        ) if ab is None else ab
    x = solveh_banded(ab, v.ravel(), lower=True)
    return x.reshape(v.shape)