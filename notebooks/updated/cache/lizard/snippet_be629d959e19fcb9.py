def cublasCtpsv(handle, uplo, trans, diag, n, AP, x, incx):
    status = _libcublas.cublasCtpsv_v2(handle, _CUBLAS_FILL_MODE[uplo],
        _CUBLAS_OP[trans], _CUBLAS_DIAG[diag], n, int(AP), int(x), incx)
    cublasCheckStatus(status)