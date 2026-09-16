def encode(epochs, iso_8601=True):
    if isinstance(epochs, int) or isinstance(epochs, np.int64):
        return CDFepoch.encode_tt2000(epochs, iso_8601)
    elif isinstance(epochs, float) or isinstance(epochs, np.float64):
        return CDFepoch.encode_epoch(epochs, iso_8601)
    elif isinstance(epochs, complex) or isinstance(epochs, np.complex128):
        return CDFepoch.encode_epoch16(epochs, iso_8601)
    elif isinstance(epochs, list) or isinstance(epochs, np.ndarray):
        if isinstance(epochs[0], int) or isinstance(epochs[0], np.int64):
            return CDFepoch.encode_tt2000(epochs, iso_8601)
        elif isinstance(epochs[0], float) or isinstance(epochs[0], np.float64):
            return CDFepoch.encode_epoch(epochs, iso_8601)
        elif isinstance(epochs[0], complex) or isinstance(epochs[0], np.
            complex128):
            return CDFepoch.encode_epoch16(epochs, iso_8601)
        else:
            print('Bad input')
            return None
    else:
        print('Bad input')
        return None