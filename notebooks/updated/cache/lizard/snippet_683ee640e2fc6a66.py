def drop_columns_with_unique_values(data: pd.DataFrame, max_unique_values:
    int=0.25):
    size = data.shape[0]
    df_uv = data.apply(lambda se: se.dropna().unique().shape[0] / size >
        max_unique_values and se.dtype in ['object', 'category'])
    data.drop(df_uv[df_uv].index, axis=1, inplace=True)