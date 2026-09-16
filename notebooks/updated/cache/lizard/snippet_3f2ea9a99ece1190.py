def schedule_snapshot(self):
    url = SNAPSHOTS_ENDPOINT
    params = SNAPSHOTS_BODY
    params['from'] = '{0}_web'.format(self.user_id)
    params['to'] = self.device_id
    params['resource'] = 'cameras/{0}'.format(self.device_id)
    params['transId'] = 'web!{0}'.format(self.xcloud_id)
    headers = {'xCloudId': self.xcloud_id}
    _LOGGER.debug('Snapshot device %s', self.name)
    _LOGGER.debug('Device params %s', params)
    _LOGGER.debug('Device headers %s', headers)
    ret = self._session.query(url, method='POST', extra_params=params,
        extra_headers=headers)
    _LOGGER.debug('Snapshot results %s', ret)
    return ret is not None and ret.get('success')