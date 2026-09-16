def metric_find(self):
    params = {'resultLimit': 50, 'resultStart': 0}
    while True:
        if params.get('resultStart') >= params.get('resultLimit'):
            break
        r = self.tcex.session.get('/v2/customMetrics', params=params)
        if not r.ok or 'application/json' not in r.headers.get('content-type',
            ''):
            self.tcex.handle_error(705, [r.status_code, r.text])
        data = r.json()
        for metric in data.get('data', {}).get('customMetricConfig'):
            if metric.get('name') == self._metric_name:
                self._metric_id = metric.get('id')
                info = 'found metric with name "{}" and Id {}.'
                self.tcex.log.info(info.format(self._metric_name, self.
                    _metric_id))
                return True
        params['resultStart'] += params.get('resultLimit')
    return False