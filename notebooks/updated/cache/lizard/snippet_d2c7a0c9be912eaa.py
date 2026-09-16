def _run_arguement_object_fits(self):
    Y_dict = self._catalog_object.get_transformed_Y()
    X = self._designmatrix_object.get_matrix()
    Xcol_names = self._designmatrix_object.get_columnnames()
    row_names = self._designmatrix_object.get_rownames()
    Y = np.empty((len(row_names), len(Y_dict[Y_dict.keys()[0]])))
    if sum(np.iscomplex(Y_dict[Y_dict.keys()[0]])):
        Y = np.empty((len(row_names), len(Y_dict[Y_dict.keys()[0]]))).astype(np
            .complex)
    for i in np.arange(0, len(row_names)):
        Y[(i), :] = Y_dict[row_names[i]]
    A = self._basis_object.fit_transform(Y)
    return Y, X, A, Xcol_names, row_names