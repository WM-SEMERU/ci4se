def get_or_create_in_transaction_wrapper(tsession, model, values,
    missing_columns=[], variable_columns=[], updatable_columns=[],
    only_use_supplied_columns=False, read_only=False):
    return get_or_create_in_transaction(tsession, model, values,
        missing_columns=missing_columns, variable_columns=variable_columns,
        updatable_columns=updatable_columns, only_use_supplied_columns=
        only_use_supplied_columns, read_only=read_only)