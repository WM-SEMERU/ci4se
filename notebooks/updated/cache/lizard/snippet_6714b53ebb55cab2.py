def __x_google_quota_descriptor(self, metric_costs):
    return {'metricCosts': {metric: cost for metric, cost in metric_costs.
        items()}} if metric_costs else None