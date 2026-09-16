def required(col_name, arg, dm, df, *args):
    if col_name in df.columns:
        return None
    else:
        return '"{}" column is required'.format(col_name)