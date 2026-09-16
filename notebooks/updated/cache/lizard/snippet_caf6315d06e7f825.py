def dropna(data: pd.DataFrame, axis: int, **params):
    if axis == 0:
        dropna_rows(data=data, **params)
    else:
        dropna_columns(data=data, **params)