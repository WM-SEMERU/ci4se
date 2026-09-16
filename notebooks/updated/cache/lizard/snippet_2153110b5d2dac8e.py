def search(df, match, columns=['Proteins', 'Protein names', 'Gene names']):
    df = df.copy()
    dft = df.reset_index()
    mask = np.zeros((dft.shape[0],), dtype=bool)
    idx = ['Proteins', 'Protein names', 'Gene names']
    for i in idx:
        if i in dft.columns:
            mask = mask | np.array([(match in str(l)) for l in dft[i].values])
    return df.iloc[mask]