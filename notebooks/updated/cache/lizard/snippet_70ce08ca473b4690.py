def event_filter_type(self, event_filter_type):
    allowed_values = ['BYCHART', 'AUTOMATIC', 'ALL', 'NONE', 'BYDASHBOARD',
        'BYCHARTANDDASHBOARD']
    if event_filter_type not in allowed_values:
        raise ValueError(
            'Invalid value for `event_filter_type` ({0}), must be one of {1}'
            .format(event_filter_type, allowed_values))
    self._event_filter_type = event_filter_type