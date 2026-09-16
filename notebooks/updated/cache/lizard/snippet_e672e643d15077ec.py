def filter_select_columns_intensity(df, prefix, columns):
    return df.filter(regex='^(%s.+|%s)$' % (prefix, '|'.join(columns)))