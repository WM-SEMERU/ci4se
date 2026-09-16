def f1_score(df, col_true=None, col_pred='precision_result', pos_label=1,
    average=None):
    r
    if not col_pred:
        col_pred = get_field_name_by_role(df, FieldRole.PREDICTED_CLASS)
    return fbeta_score(df, col_true, col_pred, pos_label=pos_label, average
        =average)