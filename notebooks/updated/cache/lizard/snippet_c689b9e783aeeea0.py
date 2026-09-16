def _load_from_file(path):
    config = []
    try:
        with open(path, 'r') as config_file:
            config = yaml.load(config_file)['normalizations']
    except EnvironmentError as e:
        raise ConfigError('Problem while loading file: %s' % e.args[1] if 
            len(e.args) > 1 else e)
    except (TypeError, KeyError) as e:
        raise ConfigError('Config file has an unexpected structure: %s' % e)
    except yaml.YAMLError:
        raise ConfigError('Invalid YAML file syntax')
    return config