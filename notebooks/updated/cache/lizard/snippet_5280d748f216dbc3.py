def main(cls):
    parser = argparse.ArgumentParser(description=
        'Server for the {} SOA service'.format(cls.service_name))
    parser.add_argument('-d', '--daemon', action='store_true', help=
        'run the server process as a daemon')
    if not cls.use_django:
        parser.add_argument('-s', '--settings', help=
            'The settings module to use', required=True)
    cmd_options, _ = parser.parse_known_args(sys.argv[1:])
    if cls.use_django:
        if not django_settings:
            raise ImportError(
                'Could not import Django. You must install Django if you enable Django support in your service.'
                )
        try:
            settings = cls.settings_class(django_settings.SOA_SERVER_SETTINGS)
        except AttributeError:
            raise ValueError(
                'Cannot find `SOA_SERVER_SETTINGS` in the Django settings.')
    else:
        try:
            settings_module = importlib.import_module(cmd_options.settings)
        except ImportError as e:
            raise ValueError('Cannot import settings module `%s`: %s' % (
                cmd_options.settings, e))
        try:
            settings_dict = getattr(settings_module, 'SOA_SERVER_SETTINGS')
        except AttributeError:
            try:
                settings_dict = getattr(settings_module, 'settings')
            except AttributeError:
                raise ValueError(
                    'Cannot find `SOA_SERVER_SETTINGS` or `settings` variable in settings module `{}`.'
                    .format(cmd_options.settings))
        settings = cls.settings_class(settings_dict)
    PySOALogContextFilter.set_service_name(cls.service_name)
    logging.config.dictConfig(settings['logging'])
    if cmd_options.daemon:
        pid = os.fork()
        if pid > 0:
            print('PID={}'.format(pid))
            sys.exit()
    server = cls.initialize(settings)(settings)
    server.run()