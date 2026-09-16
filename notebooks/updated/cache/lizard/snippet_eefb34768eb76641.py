def plan_transpose(N1, N2):
    rows = N1
    cols = N2
    iodim = numpy.zeros(6, dtype=numpy.int32)
    iodim[0] = rows
    iodim[1] = 1
    iodim[2] = cols
    iodim[3] = cols
    iodim[4] = rows
    iodim[5] = 1
    N = N1 * N2
    vin = pycbc.types.zeros(N, dtype=numpy.complex64)
    vout = pycbc.types.zeros(N, dtype=numpy.complex64)
    f = float_lib.fftwf_plan_guru_dft
    f.argtypes = [ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.
        c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes
        .c_int]
    f.restype = ctypes.c_void_p
    return f(0, None, 2, iodim.ctypes.data, vin.ptr, vout.ptr, None,
        FFTW_MEASURE)