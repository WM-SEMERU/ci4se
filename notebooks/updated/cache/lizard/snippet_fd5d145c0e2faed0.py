def config_from_prefix(prefix):
    settings = {}
    if prefix.lower() in ('default', 'auto', ''):
        settings['zmq_prefix'] = ''
        settings['libzmq_extension'] = False
        settings['no_libzmq_extension'] = False
    elif prefix.lower() in ('bundled', 'extension'):
        settings['zmq_prefix'] = ''
        settings['libzmq_extension'] = True
        settings['no_libzmq_extension'] = False
    else:
        settings['zmq_prefix'] = prefix
        settings['libzmq_extension'] = False
        settings['no_libzmq_extension'] = True
    return settings