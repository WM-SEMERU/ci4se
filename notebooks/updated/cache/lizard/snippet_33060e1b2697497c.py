def get_sos_decomposition(sdp, y_mat=None, threshold=0.0):
    if len(sdp.monomial_sets) != 1:
        raise Exception('Cannot automatically match primal and dual ' +
            'variables.')
    elif len(sdp.y_mat[1:]) != len(sdp.constraints):
        raise Exception(
            'Cannot automatically match constraints with blocks ' +
            'in the dual solution.')
    elif sdp.status == 'unsolved' and y_mat is None:
        raise Exception('The SDP relaxation is unsolved and dual solution ' +
            'is not provided!')
    elif sdp.status != 'unsolved' and y_mat is None:
        y_mat = sdp.y_mat
    sos = []
    for y_mat_block in y_mat:
        term = 0
        vals, vecs = np.linalg.eigh(y_mat_block)
        for j, val in enumerate(vals):
            if val < -0.001:
                raise Exception('Large negative eigenvalue: ' + val +
                    '. Matrix cannot be positive.')
            elif val > 0:
                sub_term = 0
                for i, entry in enumerate(vecs[:, (j)]):
                    sub_term += entry * sdp.monomial_sets[0][i]
                term += val * sub_term ** 2
        term = expand(term)
        new_term = 0
        if term.is_Mul:
            elements = [term]
        else:
            elements = term.as_coeff_mul()[1][0].as_coeff_add()[1]
        for element in elements:
            _, coeff = separate_scalar_factor(element)
            if abs(coeff) > threshold:
                new_term += element
        sos.append(new_term)
    return sos