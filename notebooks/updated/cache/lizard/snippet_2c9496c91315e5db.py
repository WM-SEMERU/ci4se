def create_autoscale_rule(subscription_id, resource_group, vmss_name,
    metric_name, operator, threshold, direction, change_count, time_grain=
    'PT1M', time_window='PT5M', cool_down='PT1M'):
    metric_trigger = {'metricName': metric_name}
    metric_trigger['metricNamespace'] = ''
    metric_trigger['metricResourceUri'] = ('/subscriptions/' +
        subscription_id + '/resourceGroups/' + resource_group +
        '/providers/Microsoft.Compute/virtualMachineScaleSets/' + vmss_name)
    metric_trigger['timeGrain'] = time_grain
    metric_trigger['statistic'] = 'Average'
    metric_trigger['timeWindow'] = time_window
    metric_trigger['timeAggregation'] = 'Average'
    metric_trigger['operator'] = operator
    metric_trigger['threshold'] = threshold
    scale_action = {'direction': direction}
    scale_action['type'] = 'ChangeCount'
    scale_action['value'] = str(change_count)
    scale_action['cooldown'] = cool_down
    new_rule = {'metricTrigger': metric_trigger}
    new_rule['scaleAction'] = scale_action
    return new_rule