def get_distinct_values_from_cols(self, l_col_list):
    uniq_vals = []
    for l_col_name in l_col_list:
        uniq_vals.append(set(self.get_col_data_by_name(l_col_name)))
    if len(l_col_list) == 0:
        return []
    elif len(l_col_list) == 1:
        return sorted([v for v in uniq_vals])
    elif len(l_col_list) == 2:
        res = []
        res = [(a, b) for a in uniq_vals[0] for b in uniq_vals[1]]
        return res
    else:
        print('TODO ')
        return -44