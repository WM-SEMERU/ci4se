def alert_statuses(self, alert_statuses):
    if alert_statuses is None:
        raise ValueError(
            'Invalid value for `alert_statuses`, must not be `None`')
    allowed_values = ['VISIBLE', 'HIDDEN', 'NOT_LOADED']
    if not set(alert_statuses.keys()).issubset(set(allowed_values)):
        raise ValueError(
            'Invalid keys in `alert_statuses` [{0}], must be a subset of [{1}]'
            .format(', '.join(map(str, set(alert_statuses.keys()) - set(
            allowed_values))), ', '.join(map(str, allowed_values))))
    self._alert_statuses = alert_statuses