def on_edited_dataframe_sync(cell_renderer, iter, new_value, column,
    df_py_dtypes, list_store, df_data):
    column_name = column.get_name()
    i, dtype = df_py_dtypes.ix[column_name]
    if dtype == float:
        value = si_parse(new_value)
    elif dtype == bool:
        value = not list_store[iter][i]
    if value == list_store[iter][i]:
        return False
    list_store[iter][i] = value
    df_data[column_name].values[int(iter)] = value
    return True