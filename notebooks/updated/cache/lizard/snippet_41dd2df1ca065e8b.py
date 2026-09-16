def create(self, create_info=None, hyperparameter=None, server='local',
    insights=False):
    if not create_info:
        create_info = {'server': server, 'config': {'insights': insights,
            'command': ' '.join(sys.argv)}}
        config = find_config(self.config_path, logger=self.logger)
        if not config['model']:
            raise Exception('AETROS config file (aetros.yml) not found.')
        full_hyperparameters = lose_parameters_to_full(config['parameters'])
        hyperparameter = extract_parameters(full_hyperparameters,
            hyperparameter)
        create_info['config']['parameters'] = hyperparameter
    self.job = create_info
    if 'server' not in self.job and server:
        self.job['server'] = server
    self.job['optimization'] = None
    self.job['type'] = 'custom'
    if 'parameters' not in self.job['config']:
        self.job['config']['parameters'] = {}
    if 'insights' not in self.job['config']:
        self.job['config']['insights'] = insights
    self.job['created'] = time.time()
    self.git.create_job_id(self.job)
    self.logger.debug('Job created with Git ref ' + self.git.ref_head)
    return self.job_id