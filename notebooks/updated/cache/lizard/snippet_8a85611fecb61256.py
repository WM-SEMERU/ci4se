def matrix_rank(model):
    s_matrix, _, _ = con_helpers.stoichiometry_matrix(model.metabolites,
        model.reactions)
    return con_helpers.rank(s_matrix)