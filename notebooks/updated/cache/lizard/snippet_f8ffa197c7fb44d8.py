def _verify(function):

    def wrapped(pin, *args, **kwargs):
        pin = int(pin)
        if pin not in _open:
            ppath = gpiopath(pin)
            if not os.path.exists(ppath):
                log.debug('Creating Pin {0}'.format(pin))
                with _export_lock:
                    with open(pjoin(gpio_root, 'export'), 'w') as f:
                        _write(f, pin)
            value = open(pjoin(ppath, 'value'), FMODE)
            direction = open(pjoin(ppath, 'direction'), FMODE)
            _open[pin] = PinState(value=value, direction=direction)
        return function(pin, *args, **kwargs)
    return wrapped