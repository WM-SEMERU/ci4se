def correlation_matrix(df):
    columns = df.columns.tolist()
    corr = pd.DataFrame(np.corrcoef(df, rowvar=0), columns=columns, index=
        columns)
    return corr