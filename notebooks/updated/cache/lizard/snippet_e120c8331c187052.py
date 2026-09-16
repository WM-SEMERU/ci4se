def clip_range(nodes1, nodes2):
    r
    coeff_a, coeff_b, coeff_c, d_min, d_max = compute_fat_line(nodes1)
    _, num_nodes2 = nodes2.shape
    polynomial = np.empty((2, num_nodes2), order='F')
    denominator = float(num_nodes2 - 1)
    for index in six.moves.xrange(num_nodes2):
        polynomial[0, index] = index / denominator
        polynomial[1, index] = coeff_a * nodes2[0, index] + coeff_b * nodes2[
            1, index] + coeff_c
    start_bottom = np.asfortranarray([0.0, d_min])
    end_bottom = np.asfortranarray([1.0, d_min])
    start_top = np.asfortranarray([0.0, d_max])
    end_top = np.asfortranarray([1.0, d_max])
    s_min = DEFAULT_S_MIN
    s_max = DEFAULT_S_MAX
    for start_index in six.moves.xrange(num_nodes2 - 1):
        for end_index in six.moves.xrange(start_index + 1, num_nodes2):
            s_min, s_max = _update_parameters(s_min, s_max, start_bottom,
                end_bottom, polynomial[:, (start_index)], polynomial[:, (
                end_index)])
            s_min, s_max = _update_parameters(s_min, s_max, start_top,
                end_top, polynomial[:, (start_index)], polynomial[:, (
                end_index)])
    return _check_parameter_range(s_min, s_max)