def add_job(self, raw_host, job_name):
    url_host_map = dict((host_dict.get('url', host_name).rstrip('/'),
        host_name) for host_name, host_dict in self._config_dict.items())
    if raw_host in self._config_dict:
        host_url = self._config_dict[raw_host].get('url', raw_host)
        host = raw_host
    elif raw_host in url_host_map:
        host_url = raw_host
        host = url_host_map[raw_host]
    else:
        host_url, host = raw_host, raw_host
    if host not in self._config_dict:
        self._config_dict[host] = {'url': host_url, 'jobs': []}
    if 'jobs' not in self._config_dict[host]:
        self._config_dict[host]['jobs'] = []
    self._config_dict[host]['jobs'].append(job_name)
    self._add_job(host, job_name, host_url=host_url)