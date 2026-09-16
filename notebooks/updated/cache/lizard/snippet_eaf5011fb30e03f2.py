def ffill_query_in_range(expr, lower, upper, checkpoints=None, odo_kwargs=
    None, ts_field=TS_FIELD_NAME):
    odo_kwargs = odo_kwargs or {}
    computed_lower, materialized_checkpoints = get_materialized_checkpoints(
        checkpoints, expr.fields, lower, odo_kwargs)
    pred = expr[ts_field] <= upper
    if computed_lower is not None:
        pred &= expr[ts_field] >= computed_lower
    raw = pd.concat((materialized_checkpoints, odo(expr[pred], pd.DataFrame,
        **odo_kwargs)), ignore_index=True)
    raw.loc[:, (ts_field)] = raw.loc[:, (ts_field)].astype('datetime64[ns]')
    return raw