def get_metric_type(measure, aggregation):
    if aggregation.aggregation_type == aggregation_module.Type.NONE:
        raise ValueError('aggregation type must not be NONE')
    assert isinstance(aggregation, AGGREGATION_TYPE_MAP[aggregation.
        aggregation_type])
    if aggregation.aggregation_type == aggregation_module.Type.SUM:
        if isinstance(measure, measure_module.MeasureInt):
            return metric_descriptor.MetricDescriptorType.CUMULATIVE_INT64
        elif isinstance(measure, measure_module.MeasureFloat):
            return metric_descriptor.MetricDescriptorType.CUMULATIVE_DOUBLE
        else:
            raise ValueError
    elif aggregation.aggregation_type == aggregation_module.Type.COUNT:
        return metric_descriptor.MetricDescriptorType.CUMULATIVE_INT64
    elif aggregation.aggregation_type == aggregation_module.Type.DISTRIBUTION:
        return metric_descriptor.MetricDescriptorType.CUMULATIVE_DISTRIBUTION
    elif aggregation.aggregation_type == aggregation_module.Type.LASTVALUE:
        if isinstance(measure, measure_module.MeasureInt):
            return metric_descriptor.MetricDescriptorType.GAUGE_INT64
        elif isinstance(measure, measure_module.MeasureFloat):
            return metric_descriptor.MetricDescriptorType.GAUGE_DOUBLE
        else:
            raise ValueError
    else:
        raise AssertionError