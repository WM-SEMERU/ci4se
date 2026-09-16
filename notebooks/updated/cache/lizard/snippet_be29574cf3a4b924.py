def merge(cls, tables, fillna=False):
    cols = set(itertools.chain(*[table.dtype.descr for table in tables]))
    tables_to_merge = []
    for table in tables:
        missing_cols = cols - set(table.dtype.descr)
        if missing_cols:
            if fillna:
                n = len(table)
                n_cols = len(missing_cols)
                col_names = []
                for col_name, col_dtype in missing_cols:
                    if 'f' not in col_dtype:
                        raise ValueError(
                            "Cannot create NaNs for non-float type column '{}'"
                            .format(col_name))
                    col_names.append(col_name)
                table = table.append_columns(col_names, np.full((n_cols, n),
                    np.nan))
            else:
                raise ValueError(
                    'Table columns do not match. Use fill_na=True if you want to append missing values with NaNs'
                    )
        tables_to_merge.append(table)
    first_table = tables_to_merge[0]
    merged_table = sum(tables_to_merge[1:], first_table)
    merged_table.h5loc = first_table.h5loc
    merged_table.h5singleton = first_table.h5singleton
    merged_table.split_h5 = first_table.split_h5
    merged_table.name = first_table.name
    return merged_table