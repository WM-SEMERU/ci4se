def get_client_ip(self):
    if self.client_ip:
        return self.client_ip
    try:
        client = os.environ.get('SSH_CONNECTION', os.environ.get('SSH_CLIENT'))
        self.client_ip = client.split()[0]
        self.logdebug('client_ip: %s\n' % self.client_ip)
        return self.client_ip
    except:
        raise SSHEnvironmentError('cannot identify the ssh client IP address')