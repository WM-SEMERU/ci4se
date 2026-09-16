def fill_categorical_na(df, nan_cat='NA'):
    for col in df.columns[df.isna().any()].tolist():
        if df[col].dtype.name != 'category':
            df[col] = df[col].fillna('')
        else:
            try:
                df[col].cat.add_categories([nan_cat], inplace=True)
            except ValueError:
                pass
            df[col] = df[col].fillna(nan_cat)
    return df