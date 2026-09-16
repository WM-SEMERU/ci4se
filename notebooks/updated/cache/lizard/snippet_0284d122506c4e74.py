def _ensure_timestamp_field(dataset_expr, deltas, checkpoints):
    measure = dataset_expr.dshape.measure
    if TS_FIELD_NAME not in measure.names:
        dataset_expr = bz.transform(dataset_expr, **{TS_FIELD_NAME:
            dataset_expr[AD_FIELD_NAME]})
        deltas = _ad_as_ts(deltas)
        checkpoints = _ad_as_ts(checkpoints)
    else:
        _check_datetime_field(TS_FIELD_NAME, measure)
    return dataset_expr, deltas, checkpoints