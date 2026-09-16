def notes(path):
    df = pd.read_csv(path, delimiter='\t')
    text_row = df.iloc[0:-1, (0)].str.contains('[a-z]', '[A-Z]')
    text_row_index = text_row.index[text_row].tolist()
    notes = df.loc[text_row_index]
    return notes