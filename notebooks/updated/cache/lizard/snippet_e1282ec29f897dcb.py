def _enable_pin(pin, direction):
    _write_value(pin, '{}/export'.format(_path_prefix))
    _write_value(direction, '{0}/gpio{1}/direction'.format(_path_prefix, pin))