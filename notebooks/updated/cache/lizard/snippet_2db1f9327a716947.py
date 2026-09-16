def create_app_from_yml(path):
    try:
        with open(path, 'rt', encoding='UTF-8') as f:
            try:
                interpolated = io.StringIO(f.read() % {'here': os.path.
                    abspath(os.path.dirname(path))})
                interpolated.name = f.name
                conf = yaml.safe_load(interpolated)
            except yaml.YAMLError as exc:
                raise RuntimeError(
                    'Cannot parse a configuration file. Context: ' + str(exc))
    except FileNotFoundError:
        conf = {'metadata': None, 'pipes': {}}
    return core.create_app(conf['metadata'], pipes=conf['pipes'])