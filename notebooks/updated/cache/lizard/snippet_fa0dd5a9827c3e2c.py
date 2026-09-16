def _serial_send(self, port, payload):
    if port not in self.open_devices:
        logger.error('Error sending data: `%s` not connected', port)
        self._publish_status(port)
    else:
        try:
            device = self.open_devices[port]
            device.write(payload)
            logger.debug('Sent data to `%s`', port)
        except Exception as exception:
            logger.error('Error sending data to `%s`: %s', port, exception)