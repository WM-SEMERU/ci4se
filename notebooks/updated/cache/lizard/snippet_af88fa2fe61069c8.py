def describe_alarms_for_metric(self, metric_name, namespace, period=None,
    statistic=None, dimensions=None, unit=None):
    params = {'MetricName': metric_name, 'Namespace': namespace}
    if period:
        params['Period'] = period
    if statistic:
        params['Statistic'] = statistic
    if dimensions:
        self.build_dimension_param(dimensions, params)
    if unit:
        params['Unit'] = unit
    return self.get_list('DescribeAlarmsForMetric', params, [('member',
        MetricAlarm)])