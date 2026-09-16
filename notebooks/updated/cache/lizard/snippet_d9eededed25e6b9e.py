def dense_output(t_current, t_old, h_current, rcont):
    s = (t_current - t_old) / h_current
    s1 = 1.0 - s
    return rcont[0] + s * (rcont[1] + s1 * (rcont[2] + s * (rcont[3] + s1 *
        (rcont[4] + s * (rcont[5] + s1 * (rcont[6] + s * rcont[7]))))))