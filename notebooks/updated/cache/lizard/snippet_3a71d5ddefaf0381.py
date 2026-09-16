def _result_type_many(*arrays_and_dtypes):
    try:
        return np.result_type(*arrays_and_dtypes)
    except ValueError:
        return reduce(np.result_type, arrays_and_dtypes)