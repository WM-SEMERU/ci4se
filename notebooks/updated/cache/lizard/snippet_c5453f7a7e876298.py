def __connect(host, port, username, password, private_key):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if private_key is not None and password is not None:
        private_key = paramiko.RSAKey.from_private_key_file(private_key,
            password)
    elif private_key is not None:
        private_key = paramiko.RSAKey.from_private_key_file(private_key,
            password)
    try:
        ssh.connect(host, port, username, password, private_key)
    except Exception as e:
        raise e
    return ssh