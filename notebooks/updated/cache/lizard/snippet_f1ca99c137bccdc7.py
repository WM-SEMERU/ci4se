def ssh(host, forward_agent=False, sudoable=False, max_attempts=1,
    max_timeout=5, ssh_password=None):
    with closing(SSHClient()) as client:
        client.set_missing_host_key_policy(AutoAddPolicy())
        cfg = {'hostname': host, 'timeout': max_timeout}
        if ssh_password:
            cfg['password'] = ssh_password
        ssh_config = SSHConfig()
        user_config_file = os.path.expanduser('~/.ssh/config')
        if os.path.exists(user_config_file):
            with open(user_config_file) as f:
                ssh_config.parse(f)
                host_config = ssh_config.lookup(host)
                if 'user' in host_config:
                    cfg['username'] = host_config['user']
                if 'proxycommand' in host_config:
                    cfg['sock'] = ProxyCommand(host_config['proxycommand'])
                if 'identityfile' in host_config:
                    cfg['key_filename'] = host_config['identityfile']
                if 'port' in host_config:
                    cfg['port'] = int(host_config['port'])
        attempts = 0
        while attempts < max_attempts:
            try:
                attempts += 1
                client.connect(**cfg)
                break
            except socket.error as e:
                if attempts < max_attempts:
                    print('SSH to host {0} failed, retrying...'.format(host))
                    time.sleep(max_timeout)
                else:
                    print('SSH Exception: {0}'.format(e))
        else:
            raise MaxConnectionAttemptsError(
                'Exceeded max attempts to connect to host {0} after {1} retries'
                .format(host, max_attempts))
        yield Connection(client, forward_agent, sudoable)