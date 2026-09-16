def _parse_hostvar_file(self, hostname, path):
    first_line = open(path, 'r').readline()
    if first_line.startswith('$ANSIBLE_VAULT'):
        self.log.warning('Skipping encrypted vault file {0}'.format(path))
        return
    try:
        self.log.debug('Reading host vars from {}'.format(path))
        f = codecs.open(path, 'r', encoding='utf8')
        invars = ihateyaml.safe_load(f)
        f.close()
    except Exception as err:
        self.log.warning("Yaml couldn't load '{0}'. Skipping. Error was: {1}"
            .format(path, err))
        return
    if invars is None:
        return
    if hostname == 'all':
        for hostname in self.hosts_all():
            self.update_host(hostname, {'hostvars': invars}, overwrite=False)
    else:
        self.update_host(hostname, {'hostvars': invars}, overwrite=True)