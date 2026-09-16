def degrees_of_freedom(model):
    s_matrix, _, _ = con_helpers.stoichiometry_matrix(model.metabolites,
        model.reactions)
    return s_matrix.shape[1] - matrix_rank(model)