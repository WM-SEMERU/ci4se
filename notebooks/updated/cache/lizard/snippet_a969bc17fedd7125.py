def cli(self):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=self.private_hostname, username=self.username,
        key_filename=self.key_filename, timeout=self.timeout, look_for_keys
        =self.look_for_keys)
    transport = client.get_transport()
    transport.set_keepalive(3)
    return client