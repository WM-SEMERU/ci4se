def to_aggregation(self, metric_name=None, parent_table=None,
    backup_metric_name=None):
    op = self.op()
    arg_table = find_base_table(op.arg)
    by = op.by
    if not isinstance(by, Expr):
        by = by(arg_table)
        by_table = arg_table
    else:
        by_table = find_base_table(op.by)
    if metric_name is None:
        if by.get_name() == op.arg.get_name():
            by = by.name(backup_metric_name)
    else:
        by = by.name(metric_name)
    if arg_table.equals(by_table):
        agg = arg_table.aggregate(by, by=[op.arg])
    elif parent_table is not None:
        agg = parent_table.aggregate(by, by=[op.arg])
    else:
        raise com.IbisError(
            'Cross-table TopK; must provide a parent joined table')
    return agg.sort_by([(by.get_name(), False)]).limit(op.k)