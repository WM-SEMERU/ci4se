def cublasStrsm(handle, side, uplo, trans, diag, m, n, alpha, A, lda, B, ldb):
    status = _libcublas.cublasStrsm_v2(handle, _CUBLAS_SIDE_MODE[side],
        _CUBLAS_FILL_MODE[uplo], _CUBLAS_OP[trans], _CUBLAS_DIAG[diag], m,
        n, ctypes.byref(ctypes.c_float(alpha)), int(A), lda, int(B), ldb)
    cublasCheckStatus(status)