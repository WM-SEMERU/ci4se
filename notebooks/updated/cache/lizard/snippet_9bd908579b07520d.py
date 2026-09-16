def configure_attributes(self, json_data):
    env = boto3.session.Session(profile_name=self.env, region_name=self.region)
    elbclient = env.client('elb')
    elb_settings = self.properties['elb']
    LOG.debug('Block ELB Settings Pre Configure Load Balancer Attributes:\n%s',
        pformat(elb_settings))
    for job in json.loads(json_data)['job']:
        load_balancer_attributes = {'CrossZoneLoadBalancing': {'Enabled':
            True}, 'AccessLog': {'Enabled': False}, 'ConnectionDraining': {
            'Enabled': False}, 'ConnectionSettings': {'IdleTimeout': 60}}
        if elb_settings.get('connection_draining_timeout'):
            connection_draining_timeout = int(elb_settings[
                'connection_draining_timeout'])
            LOG.info(
                'Applying Custom Load Balancer Connection Draining Timeout: %d'
                , connection_draining_timeout)
            load_balancer_attributes['ConnectionDraining'] = {'Enabled':
                True, 'Timeout': connection_draining_timeout}
        if elb_settings.get('idle_timeout'):
            idle_timeout = int(elb_settings['idle_timeout'])
            LOG.info('Applying Custom Load Balancer Idle Timeout: %d',
                idle_timeout)
            load_balancer_attributes['ConnectionSettings'] = {'IdleTimeout':
                idle_timeout}
        if elb_settings.get('access_log'):
            access_log_bucket_name = elb_settings['access_log']['bucket_name']
            access_log_bucket_prefix = elb_settings['access_log'][
                'bucket_prefix']
            access_log_emit_interval = int(elb_settings['access_log'][
                'emit_interval'])
            LOG.info(
                'Applying Custom Load Balancer Access Log: %s/%s every %d minutes'
                , access_log_bucket_name, access_log_bucket_prefix,
                access_log_emit_interval)
            load_balancer_attributes['AccessLog'] = {'Enabled': True,
                'S3BucketName': access_log_bucket_name, 'EmitInterval':
                access_log_emit_interval, 'S3BucketPrefix':
                access_log_bucket_prefix}
        LOG.info('Applying Load Balancer Attributes')
        LOG.debug('Load Balancer Attributes:\n%s', pformat(
            load_balancer_attributes))
        elbclient.modify_load_balancer_attributes(LoadBalancerName=self.app,
            LoadBalancerAttributes=load_balancer_attributes)