def round_to_n_decimal_places(array, n=3):
    if issubclass(array.__class__, float) and '%.e' % array == str(array):
        return array
    shape = np.shape(array)
    out = (np.atleast_1d(array) * 10 ** n).round().astype('int') / 10.0 ** n
    return out.reshape(shape)