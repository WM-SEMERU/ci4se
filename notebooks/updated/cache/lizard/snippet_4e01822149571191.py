def read_srml(filename):
    tsv_data = pd.read_csv(filename, delimiter='\t')
    data = format_index(tsv_data)
    data = data[data.columns[2:]]
    data = data.rename(columns=map_columns)
    columns = data.columns
    flag_label_map = {flag: (columns[columns.get_loc(flag) - 1] + '_flag') for
        flag in columns[1::2]}
    data = data.rename(columns=flag_label_map)
    for col in columns[::2]:
        missing = data[col + '_flag'] == 99
        data[col] = data[col].where(~missing, np.NaN)
    return data