def load_config(cls, configfile='logging.yaml'):
    configfile = getenv(cls.CONFIGFILE_ENV_KEY, configfile)
    if isfile(configfile):
        with open(configfile, 'r') as cf:
            try:
                dictConfig(load(cf))
            except ValueError:
                debug('Learn to config foooo! Improper config at %s',
                    configfile)
            except Exception:
                exception('Something went wrong while reading %s.', configfile)
    else:
        raise ValueError('Invalid configfile specified: {}'.format(configfile))