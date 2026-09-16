def total_sum_of_squares(df, col_true, col_pred=None):
    if not col_pred:
        col_pred = get_field_name_by_role(df, FieldRole.PREDICTED_VALUE)
    return _run_evaluation_node(df, col_true, col_pred)['sst']