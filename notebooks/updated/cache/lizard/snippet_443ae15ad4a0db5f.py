def _generate_output_dataframe(data_subset, defaults):
    cols = set(data_subset.columns)
    desired_cols = set(defaults)
    data_subset.drop(cols - desired_cols, axis=1, inplace=True)
    for col in (desired_cols - cols):
        data_subset[col] = defaults[col](data_subset, col)
    return data_subset