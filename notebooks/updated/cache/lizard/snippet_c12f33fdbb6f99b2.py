def __do_case_5_work(d_w, d_u, case_1, case_2, case_3, dfs_data):
    if case_3:
        return False
    comp_d_w = abs(d_w)
    __insert_frond_LF(d_w, d_u, dfs_data)
    m = dfs_data['FG']['m']
    Lm = L(m, dfs_data)
    if comp_d_w < Lm['u']:
        Lm['u'] = d_w
    if d_u > Lm['v']:
        Lm['v'] = d_u
    if case_2:
        Lm['u'] = d_w
        x_m1 = fn_x(m - 1, dfs_data)
        while comp_d_w < x_m1:
            merge_Fm(dfs_data)
            m = dfs_data['FG']['m']
            x_m1 = fn_x(m - 1, dfs_data)
    return True