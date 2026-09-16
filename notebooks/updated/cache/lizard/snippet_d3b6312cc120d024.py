def fetch_all(self, credentials, regions=[], partition_name='aws', targets=None
    ):
    global status, formatted_string
    if not targets:
        targets = type(self).targets
    printInfo('Fetching %s config...' % format_service_name(self.service))
    formatted_string = None
    api_service = self.service.lower()
    if self.service in ['s3']:
        api_clients = {}
        for region in build_region_list(self.service, regions, partition_name):
            api_clients[region] = connect_service('s3', credentials, region,
                silent=True)
        api_client = api_clients[list(api_clients.keys())[0]]
    elif self.service == 'route53domains':
        api_client = connect_service(self.service, credentials, 'us-east-1',
            silent=True)
    else:
        api_client = connect_service(self.service, credentials, silent=True)
    params = {'api_client': api_client}
    if self.service in ['s3']:
        params['api_clients'] = api_clients
    q = self._init_threading(self.__fetch_target, params, self.
        thread_config['parse'])
    params = {'api_client': api_client, 'q': q}
    if self.service in ['s3']:
        params['api_clients'] = api_clients
    qt = self._init_threading(self.__fetch_service, params, self.
        thread_config['list'])
    self.fetchstatuslogger = FetchStatusLogger(targets)
    for target in targets:
        qt.put(target)
    qt.join()
    q.join()
    if self.service != 'iam':
        self.fetchstatuslogger.show(True)