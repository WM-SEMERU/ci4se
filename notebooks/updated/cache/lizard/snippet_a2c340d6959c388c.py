def _check_constant_value_data(self, data):
    arrayval = data.flat[0]
    if np.all(data == arrayval):
        return arrayval
    return None