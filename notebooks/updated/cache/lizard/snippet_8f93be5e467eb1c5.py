def execute_ccm_remotely(remote_options, ccm_args):
    if not PARAMIKO_IS_AVAILABLE:
        logging.warn(
            'Paramiko is not Availble: Skipping remote execution of CCM command'
            )
        return None, None
    ssh_client = SSHClient(remote_options.ssh_host, remote_options.ssh_port,
        remote_options.ssh_username, remote_options.ssh_password,
        remote_options.ssh_private_key)
    for index, argument in enumerate(ccm_args):
        if '--dse-credentials' in argument:
            tokens = argument.split('=')
            credentials_path = os.path.join(os.path.expanduser('~'), '.ccm',
                '.dse.ini')
            if len(tokens) == 2:
                credentials_path = tokens[1]
            if not os.path.isfile(credentials_path):
                raise Exception('DSE Credentials File Does not Exist: %s' %
                    credentials_path)
            ssh_client.put(credentials_path, ssh_client.ccm_config_dir)
            ccm_args[index] = '--dse-credentials'
        if '--ssl' in argument or '--node-ssl' in argument:
            tokens = argument.split('=')
            if len(tokens) != 2:
                raise Exception('Path is not Specified: %s' % argument)
            ssl_path = tokens[1]
            if not os.path.isdir(ssl_path):
                raise Exception('Path Does not Exist: %s' % ssl_path)
            remote_ssl_path = ssh_client.temp + os.path.basename(ssl_path)
            ssh_client.put(ssl_path, remote_ssl_path)
            ccm_args[index] = tokens[0] + '=' + remote_ssl_path
    return ssh_client.execute_ccm_command(ccm_args)