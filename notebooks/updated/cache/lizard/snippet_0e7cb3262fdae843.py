def onSettingsChange(self, plugin_name, data):
    logger.info('onSettingsChange: {}'.format(data))
    if not plugin_name:
        logger.error('Missing plugin name')
        return
    if not data:
        logger.error('Missing data')
        return
    logger.info('Sending data {}'.format(data))
    reactor.callFromThread(self._sendJSON, {'msg': 'plugin_data_set',
        'plugin_name': plugin_name, 'data': data})
    reactor.callFromThread(self._sendJSON, {'msg': 'plugin_data_get',
        'plugin_name': plugin_name})