def _combine_results(self, match_as_dict):
    keys = []
    vals = []
    for k, v in six.iteritems(match_as_dict):
        if k[-2:] in '_a_b_c_d_e_f_g_h_i_j_k_l_m':
            if v:
                keys.append(k[:-2])
                vals.append(v)
        elif k not in keys:
            keys.append(k)
            vals.append(v)
    return dict(zip(keys, vals))