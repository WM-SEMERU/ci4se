def _count_localizations(df):
    grp = df.groupby(_index_columns)
    counts = grp['DP AA'].apply(lambda x: count(x.str.split(';').values))
    counts.index = counts.index.set_names('DP AA', level=4)
    counts.name = 'DP AA count'
    best_localization = counts.reset_index().groupby(_index_columns).apply(
        _frequent_localizations)
    return best_localization