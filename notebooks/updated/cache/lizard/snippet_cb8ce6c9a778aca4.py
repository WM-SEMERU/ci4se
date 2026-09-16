def detect_available_configs(interfaces=None):
    if interfaces is None:
        interfaces = BACKENDS.keys()
    elif isinstance(interfaces, basestring):
        interfaces = [interfaces]
    result = []
    for interface in interfaces:
        try:
            bus_class = _get_class_for_interface(interface)
        except ImportError:
            log_autodetect.debug(
                'interface "%s" can not be loaded for detection of available configurations'
                , interface)
            continue
        try:
            available = list(bus_class._detect_available_configs())
        except NotImplementedError:
            log_autodetect.debug(
                'interface "%s" does not support detection of available configurations'
                , interface)
        else:
            log_autodetect.debug(
                'interface "%s" detected %i available configurations',
                interface, len(available))
            for config in available:
                if 'interface' not in config:
                    config['interface'] = interface
            result += available
    return result