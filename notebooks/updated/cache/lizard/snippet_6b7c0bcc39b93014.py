def column_of_data(path, start, column, end='-1', units=''):
    if not isinstance(start, int):
        start = int(start)
    if not isinstance(end, int):
        end = int(end)
    df = pd.read_csv(path, delimiter='\t')
    if units == '':
        if isinstance(column, int):
            data = np.array(pd.to_numeric(df.iloc[start:end, (column)]))
        else:
            df[column][0:len(df)]
    elif isinstance(column, int):
        data = np.array(pd.to_numeric(df.iloc[start:end, (column)])) * u(units)
    else:
        df[column][0:len(df)] * u(units)
    return data