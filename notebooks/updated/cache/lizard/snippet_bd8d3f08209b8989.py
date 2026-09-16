def clean(df, error_rate=0):
    df = df.copy()
    basics.clean_colnames(df)
    print('Changed colnames to {}'.format(df.columns))
    obj_col_list = df.select_dtypes(include='object').columns
    for col_name in obj_col_list:
        df[col_name] = basics.col_strip(df, col_name)
        print("Stripped extra whitespace from '{}'".format(col_name))
    for col_name in obj_col_list:
        new_dtype = coerce_col(df, col_name, error_rate)
        if new_dtype is not None:
            print("Coerced '{}' to datatype '{}'".format(col_name, new_dtype))
    obj_col_list = df.select_dtypes(include='object').columns
    for col_name in obj_col_list:
        scrubf, scrubb = smart_scrub(df, col_name, 1 - error_rate)
        if scrubf is not None or scrubb is not None:
            print(
                "Scrubbed '{}' from the front and '{}' from the back of column '{}'"
                .format(scrubf, scrubb, col_name))
    for col_name in obj_col_list:
        new_dtype = coerce_col(df, col_name, error_rate)
        if new_dtype is not None:
            print("Coerced '{}' to datatype '{}'".format(col_name, new_dtype))
    return df