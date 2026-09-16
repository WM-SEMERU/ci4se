def get_ssh_client(ip_addr, ssh_key=None, host_name=None, ssh_tries=None,
    propagate_fail=True, username='root', password='123456'):
    host_name = host_name or ip_addr
    with LogTask('Get ssh client for %s' % host_name, level='debug',
        propagate_fail=propagate_fail):
        ssh_timeout = int(config.get('ssh_timeout'))
        if ssh_tries is None:
            ssh_tries = int(config.get('ssh_tries', 10))
        start_time = time.time()
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        while ssh_tries > 0:
            try:
                client.connect(ip_addr, username=username, password=
                    password, key_filename=ssh_key, timeout=ssh_timeout)
                break
            except (socket.error, socket.timeout) as err:
                LOGGER.debug('Socket error connecting to %s: %s', host_name,
                    err)
            except paramiko.ssh_exception.SSHException as err:
                LOGGER.debug('SSH error connecting to %s: %s', host_name, err)
            except EOFError as err:
                LOGGER.debug('EOFError connecting to %s: %s', host_name, err)
            ssh_tries -= 1
            LOGGER.debug('Still got %d tries for %s', ssh_tries, host_name)
            time.sleep(1)
        else:
            end_time = time.time()
            raise LagoSSHTimeoutException(
                'Timed out (in %d s) trying to ssh to %s' % (end_time -
                start_time, host_name))
    return client