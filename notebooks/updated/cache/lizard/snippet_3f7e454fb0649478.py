def _standard_params(klass, ids, metric_groups, **kwargs):
    end_time = kwargs.get('end_time', datetime.utcnow())
    start_time = kwargs.get('start_time', end_time - timedelta(seconds=604800))
    granularity = kwargs.get('granularity', GRANULARITY.HOUR)
    placement = kwargs.get('placement', PLACEMENT.ALL_ON_TWITTER)
    params = {'metric_groups': ','.join(metric_groups), 'start_time':
        to_time(start_time, granularity), 'end_time': to_time(end_time,
        granularity), 'granularity': granularity.upper(), 'entity': klass.
        ANALYTICS_MAP[klass.__name__], 'placement': placement}
    params['entity_ids'] = ','.join(ids)
    return params