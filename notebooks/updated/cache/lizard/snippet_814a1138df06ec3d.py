def graph_from_cov_df(df, threshold=0.5, gain=2.0, n=None, class_dict=CLASSES):
    n = n or len(df)
    nodes = [{'group': class_dict.get(name, 0), 'name': name} for name in
        df.index.values][:n]
    edges = []
    for i, (row_name, row) in enumerate(df.iterrows()):
        for j, value in enumerate(row.values):
            if i > j and value * gain > threshold and i < n and j < n:
                edges += [{'source': i, 'target': j, 'value': gain * value}]
    return nodes, edges