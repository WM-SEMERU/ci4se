def _ordered_categories(df, categories):
    for col, cats in categories.items():
        df[col] = df[col].astype(CategoricalDtype(cats, ordered=True))
    return df