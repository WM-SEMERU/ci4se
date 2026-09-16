def _get_str_columns(sf):
    return [name for name in sf.column_names() if sf[name].dtype == str]