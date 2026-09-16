def to_yaml(value, pretty=False):
    if not yaml:
        raise NotImplementedError('No supported YAML library available')
    options = {'Dumper': BasicYamlDumper, 'allow_unicode': True}
    options['default_flow_style'] = not pretty
    return yaml.dump(value, **options).rstrip()