def cublasDsbmv(handle, uplo, n, k, alpha, A, lda, x, incx, beta, y, incy):
    status = _libcublas.cublasDsbmv_v2(handle, _CUBLAS_FILL_MODE[uplo], n,
        k, ctypes.byref(ctypes.c_double(alpha)), int(A), lda, int(x), incx,
        ctypes.byref(ctypes.c_double(beta)), int(y), incy)
    cublasCheckStatus(status)