def loads(text):
    if text.startswith('CCSDS_OEM_VERS'):
        func = _read_oem
    elif text.startswith('CCSDS_OPM_VERS'):
        func = _read_opm
    else:
        raise ValueError('Unknown CCSDS type')
    return func(text)