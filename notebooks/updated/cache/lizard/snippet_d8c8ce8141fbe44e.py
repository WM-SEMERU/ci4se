def cublasDsymm(handle, side, uplo, m, n, alpha, A, lda, B, ldb, beta, C, ldc):
    status = _libcublas.cublasDsymm_v2(handle, _CUBLAS_SIDE_MODE[side],
        _CUBLAS_FILL_MODE[uplo], m, n, ctypes.byref(ctypes.c_double(alpha)),
        int(A), lda, int(B), ldb, ctypes.byref(ctypes.c_double(beta)), int(
        C), ldc)
    cublasCheckStatus(status)