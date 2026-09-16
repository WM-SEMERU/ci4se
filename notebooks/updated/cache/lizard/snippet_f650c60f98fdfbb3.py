def average_precision_score(df, col_true=None, col_pred=None, col_scores=
    None, pos_label=1):
    if not col_pred:
        col_pred = get_field_name_by_role(df, FieldRole.PREDICTED_CLASS)
    if not col_scores:
        col_scores = get_field_name_by_role(df, FieldRole.PREDICTED_SCORE)
    thresh, tp, fn, tn, fp = _run_roc_node(df, pos_label, col_true,
        col_pred, col_scores)
    precisions = np.squeeze(np.asarray(tp * 1.0 / (tp + fp)))
    recalls = np.squeeze(np.asarray(tp * 1.0 / (tp + fn)))
    return np.trapz(precisions, recalls)