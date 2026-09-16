def parse_dates(df, inplace=True, *args, **kwargs):
    if not inplace:
        df = df.copy()
    for c in df.columns:
        i = df[c].first_valid_index()
        if i is not None and type(df[c].ix[i]) in (date, datetime):
            df[c] = pd.to_datetime(df[c], *args, **kwargs)
    if not inplace:
        return df