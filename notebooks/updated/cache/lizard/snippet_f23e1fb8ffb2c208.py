def set_acceleration(self, settings):
    self._acceleration.update(settings)
    values = ['{}{}'.format(axis.upper(), value) for axis, value in sorted(
        settings.items())]
    command = '{} {}'.format(GCODES['ACCELERATION'], ' '.join(values))
    log.debug('set_acceleration: {}'.format(command))
    self._send_command(command)