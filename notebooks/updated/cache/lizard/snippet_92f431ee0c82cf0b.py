def add_configuration(self, configuration, collect_another_source, done,
    result, src):
    if 'includes' in result:
        for include in result['includes']:
            collect_another_source(include)
    configuration.update(result, source=src)