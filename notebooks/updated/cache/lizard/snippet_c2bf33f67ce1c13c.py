def dtypes_summary(df):
    output_df = pd.DataFrame([])
    row_count = df.shape[0]
    row_indexes = ['rows_numerical', 'rows_string', 'rows_date_time',
        'category_count', 'largest_category', 'rows_na', 'rows_total']
    for colname in df:
        data = df[colname]
        rows_numerical = pd.to_numeric(data, errors='coerce').count()
        rows_string = row_count - rows_numerical
        rows_date_time = pd.to_datetime(data, errors='coerce',
            infer_datetime_format=True).count()
        value_counts = data.value_counts().reset_index()
        categories = len(value_counts)
        largest_category = value_counts.iloc[0, 1]
        rows_na = data.isnull().sum()
        output_data = [rows_numerical, rows_string, rows_date_time,
            categories, largest_category, rows_na, row_count]
        output_df.loc[:, (colname)] = pd.Series(output_data)
    output_df.index = row_indexes
    return output_df