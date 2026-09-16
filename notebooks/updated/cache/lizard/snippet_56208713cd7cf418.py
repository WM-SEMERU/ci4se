def raw_to_central(n_counter, species, k_counter):
    central_in_terms_of_raw = []
    for n_iter in n_counter:
        if n_iter.order == 0:
            continue
        n_vec = n_iter.n_vector
        k_lower = [k for k in k_counter if n_iter >= k]
        n_choose_k_vec = [make_k_chose_e(k_vec.n_vector, n_vec) for k_vec in
            k_lower]
        minus_one_pow_n_min_k_vec = [_make_min_one_pow_n_minus_k(n_vec,
            k_vec.n_vector) for k_vec in k_lower]
        alpha_vec = [_make_alpha(n_vec, k_vec.n_vector, species) for k_vec in
            k_lower]
        beta_vec = [k_vec.symbol for k_vec in k_lower]
        product = [(n * m * a * b) for n, m, a, b in zip(n_choose_k_vec,
            minus_one_pow_n_min_k_vec, alpha_vec, beta_vec)]
        central_in_terms_of_raw.append(sum(product))
    return sp.Matrix(central_in_terms_of_raw)