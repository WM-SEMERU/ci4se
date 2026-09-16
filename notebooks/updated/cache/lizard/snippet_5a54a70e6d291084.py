def submit(self, cmd_string, blocksize, job_name='parsl.auto'):
    if not self.resources:
        job_name = '{0}-{1}'.format(job_name, time.time()).split('.')[0]
        self.deployment_name = '{}-{}-deployment'.format(job_name, str(time
            .time()).split('.')[0])
        formatted_cmd = template_string.format(command=cmd_string,
            overrides=self.config['execution']['block']['options'].get(
            'overrides', ''))
        print('Creating replicas :', self.init_blocks)
        self.deployment_obj = self._create_deployment_object(job_name, self
            .image, self.deployment_name, cmd_string=formatted_cmd,
            replicas=self.init_blocks)
        logger.debug('Deployment name :{}'.format(self.deployment_name))
        self._create_deployment(self.deployment_obj)
        self.resources[self.deployment_name] = {'status': 'RUNNING', 'pods':
            self.init_blocks}
    return self.deployment_name