def read_csv_with_errors(cls, url, delimiter=',', header=True, comment_char
    ='', escape_char='\\', double_quote=True, quote_char='"',
    skip_initial_space=True, column_type_hints=None, na_values=['NA'],
    line_terminator='\n', usecols=[], nrows=None, skiprows=0, verbose=True,
    nrows_to_infer=100, true_values=[], false_values=[],
    _only_raw_string_substitutions=False, **kwargs):
    return cls._read_csv_impl(url, delimiter=delimiter, header=header,
        error_bad_lines=False, comment_char=comment_char, escape_char=
        escape_char, double_quote=double_quote, quote_char=quote_char,
        skip_initial_space=skip_initial_space, column_type_hints=
        column_type_hints, na_values=na_values, line_terminator=
        line_terminator, usecols=usecols, nrows=nrows, verbose=verbose,
        skiprows=skiprows, store_errors=True, nrows_to_infer=nrows_to_infer,
        true_values=true_values, false_values=false_values,
        _only_raw_string_substitutions=_only_raw_string_substitutions, **kwargs
        )