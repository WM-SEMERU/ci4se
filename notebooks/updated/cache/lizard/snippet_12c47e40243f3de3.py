def _normalize_window(window, nfft, library, dtype):
    if library == '_lal' and isinstance(window, numpy.ndarray):
        from ._lal import window_from_array
        return window_from_array(window)
    if library == '_lal':
        from ._lal import generate_window
        return generate_window(nfft, window=window, dtype=dtype)
    if isinstance(window, string_types):
        window = canonical_name(window)
    if isinstance(window, string_types + (tuple,)):
        return get_window(window, nfft)
    return None