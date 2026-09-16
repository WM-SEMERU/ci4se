def write_calculations_to_csv(funcs, states, columns, path, headers,
    out_name, metaids=[], extension='.xls'):
    if not isinstance(funcs, list):
        funcs = [funcs] * len(headers)
    if not isinstance(states, list):
        states = [states] * len(headers)
    if not isinstance(columns, list):
        columns = [columns] * len(headers)
    data_agg = []
    for i in range(len(headers)):
        ids, data = read_state_with_metafile(funcs[i], states[i], columns[i
            ], path, metaids, extension)
        data_agg = np.append(data_agg, [data])
    output = pd.DataFrame(data=np.vstack((ids, data_agg)).T, columns=['ID'] +
        headers)
    output.to_csv(out_name, sep='\t')
    return output