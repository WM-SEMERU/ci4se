def _build_command(self):
    command = [self._path]
    command.extend(['-N1'])
    command.extend(['-l', 'dynamips_i{}_log.txt'.format(self._id)])
    if self._console_host != '0.0.0.0' and self._console_host != '::':
        command.extend(['-H', '{}:{}'.format(self._host, self._port)])
    else:
        command.extend(['-H', str(self._port)])
    return command