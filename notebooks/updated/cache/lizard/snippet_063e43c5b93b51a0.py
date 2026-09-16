def _possibly_convert_objects(values):
    return np.asarray(pd.Series(values.ravel())).reshape(values.shape)