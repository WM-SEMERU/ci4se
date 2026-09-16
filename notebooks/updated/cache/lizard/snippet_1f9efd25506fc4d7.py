def cublasZhpr2(handle, uplo, n, alpha, x, inx, y, incy, AP):
    status = _libcublas.cublasZhpr2_v2(handle, _CUBLAS_FILL_MODE[uplo], n,
        ctypes.byref(cuda.cuDoubleComplex(alpha.real, alpha.imag)), int(x),
        incx, int(y), incy, int(AP))
    cublasCheckStatus(status)