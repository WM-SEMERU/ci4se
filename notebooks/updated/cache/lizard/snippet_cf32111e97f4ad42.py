def get_external_host_tags(self):
    self.log.debug('Sending external_host_tags now')
    external_host_tags = []
    for instance in self.instances:
        i_key = self._instance_key(instance)
        if not self.mor_cache.contains(i_key):
            self.log.warning(
                'Unable to extract host tags for vSphere instance: {}'.
                format(i_key))
            continue
        for _, mor in self.mor_cache.mors(i_key):
            hostname = mor.get('hostname')
            if hostname:
                external_host_tags.append((hostname, {SOURCE_TYPE: mor.get(
                    'tags')}))
    return external_host_tags