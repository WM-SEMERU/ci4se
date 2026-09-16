def wigner_ville_spectrum(data, delta, time_bandwidth=3.5, number_of_tapers
    =None, smoothing_filter=None, filter_width=100, frequency_divider=1,
    verbose=False):
    data = np.require(data, 'float32')
    mt = _MtspecType('float32')
    npts = len(data)
    if number_of_tapers is None:
        number_of_tapers = int(2 * time_bandwidth) - 1
    if not smoothing_filter:
        smoothing_filter = 0
    elif smoothing_filter == 'boxcar':
        smoothing_filter = 1
    elif smoothing_filter == 'gauss':
        smoothing_filter = 2
    else:
        msg = 'Invalid value for smoothing filter.'
        raise Exception(msg)
    if verbose:
        verbose = C.byref(C.c_char('y'))
    else:
        verbose = None
    output = mt.empty((npts // 2 // int(frequency_divider) + 1, npts))
    mtspeclib.wv_spec_to_array_(C.byref(C.c_int(npts)), C.byref(C.c_float(
        delta)), mt.p(data), mt.p(output), C.byref(C.c_float(time_bandwidth
        )), C.byref(C.c_int(number_of_tapers)), C.byref(C.c_int(
        smoothing_filter)), C.byref(C.c_float(filter_width)), C.byref(C.
        c_int(frequency_divider)), verbose)
    return output