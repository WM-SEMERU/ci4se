def _key_opts(self):
    options = ['KbdInteractiveAuthentication=no']
    if self.passwd:
        options.append('PasswordAuthentication=yes')
    else:
        options.append('PasswordAuthentication=no')
    if self.opts.get('_ssh_version', (0,)) > (4, 9):
        options.append('GSSAPIAuthentication=no')
    options.append('ConnectTimeout={0}'.format(self.timeout))
    if self.opts.get('ignore_host_keys'):
        options.append('StrictHostKeyChecking=no')
    if self.opts.get('no_host_keys'):
        options.extend(['StrictHostKeyChecking=no',
            'UserKnownHostsFile=/dev/null'])
    known_hosts = self.opts.get('known_hosts_file')
    if known_hosts and os.path.isfile(known_hosts):
        options.append('UserKnownHostsFile={0}'.format(known_hosts))
    if self.port:
        options.append('Port={0}'.format(self.port))
    if self.priv and self.priv != 'agent-forwarding':
        options.append('IdentityFile={0}'.format(self.priv))
    if self.user:
        options.append('User={0}'.format(self.user))
    if self.identities_only:
        options.append('IdentitiesOnly=yes')
    ret = []
    for option in options:
        ret.append('-o {0} '.format(option))
    return ''.join(ret)