def filter_threshold(df, inst_rc, threshold, num_occur=1):
    from copy import deepcopy
    inst_df = deepcopy(df['mat'])
    if inst_rc == 'col':
        inst_df = inst_df.transpose()
    inst_df = inst_df.abs()
    ini_rows = inst_df.index.values.tolist()
    inst_df[inst_df < threshold] = 0
    inst_df[inst_df >= threshold] = 1
    tmp_sum = inst_df.sum(axis=1)
    tmp_sum = tmp_sum[tmp_sum >= num_occur]
    keep_names = tmp_sum.index.values.tolist()
    if inst_rc == 'row':
        if len(keep_names) < len(ini_rows):
            df['mat'] = grab_df_subset(df['mat'], keep_rows=keep_names)
            if 'mat_up' in df:
                df['mat_up'] = grab_df_subset(df['mat_up'], keep_rows=
                    keep_names)
                df['mat_dn'] = grab_df_subset(df['mat_dn'], keep_rows=
                    keep_names)
            if 'mat_orig' in df:
                df['mat_orig'] = grab_df_subset(df['mat_orig'], keep_rows=
                    keep_names)
    elif inst_rc == 'col':
        inst_df = inst_df.transpose()
        inst_rows = inst_df.index.values.tolist()
        inst_cols = keep_names
        df['mat'] = grab_df_subset(df['mat'], inst_rows, inst_cols)
        if 'mat_up' in df:
            df['mat_up'] = grab_df_subset(df['mat_up'], inst_rows, inst_cols)
            df['mat_dn'] = grab_df_subset(df['mat_dn'], inst_rows, inst_cols)
        if 'mat_orig' in df:
            df['mat_orig'] = grab_df_subset(df['mat_orig'], inst_rows,
                inst_cols)
    return df