def find_peaks_indexes(arr, window_width=5, threshold=0.0, fpeak=0):
    _check_window_width(window_width)
    if fpeak < 0 or fpeak + 1 >= window_width:
        raise ValueError('fpeak must be in the range 0- window_width - 2')
    kernel_peak = kernel_peak_function(threshold, fpeak)
    out = generic_filter(arr, kernel_peak, window_width, mode='reflect')
    result, = numpy.nonzero(out)
    return filter_array_margins(arr, result, window_width)