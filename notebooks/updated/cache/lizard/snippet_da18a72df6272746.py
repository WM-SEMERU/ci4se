def setup_from_yamlfile(self, yamlfile, output_shell=False):
    self.logger.debug('Loading config from ' + yamlfile)
    with open(yamlfile, 'r') as yamlfd:
        yamlconfig = yaml.load(yamlfd)
        for instance in yamlconfig['Instances']:
            self.add_instance(instance['role'].upper(), instance,
                output_shell=output_shell)
        if 'Config' in yamlconfig.keys():
            self.logger.debug('Config found: ' + str(yamlconfig['Config']))
            self.config = yamlconfig['Config'].copy()