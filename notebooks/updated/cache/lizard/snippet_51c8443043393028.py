def check_aggregate_region(self, variable, region='World', subregions=None,
    components=None, exclude_on_fail=False, **kwargs):
    df_subregions = self.aggregate_region(variable, region, subregions,
        components)
    if df_subregions is None:
        return
    rows = self._apply_filters(region=region, variable=variable)
    df_region, df_subregions = _aggregate(self.data[rows], ['region',
        'variable']).align(df_subregions)
    diff = df_region[~np.isclose(df_region, df_subregions, **kwargs)]
    if len(diff):
        msg = '`{}` - {} of {} rows are not aggregates of subregions'
        logger().info(msg.format(variable, len(diff), len(df_region)))
        if exclude_on_fail:
            self._exclude_on_fail(diff.index.droplevel([2, 3]))
        col_args = dict(region=region, variable=variable)
        return IamDataFrame(diff, **col_args).timeseries()