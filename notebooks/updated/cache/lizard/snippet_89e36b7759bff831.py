def _numeric_summary(arg, exact_nunique=False, prefix=None):
    metrics = [arg.count(), arg.isnull().sum().name('nulls'), arg.min(),
        arg.max(), arg.sum(), arg.mean()]
    if exact_nunique:
        unique_metric = arg.nunique().name('nunique')
    else:
        unique_metric = arg.approx_nunique().name('approx_nunique')
    metrics.append(unique_metric)
    return _wrap_summary_metrics(metrics, prefix)