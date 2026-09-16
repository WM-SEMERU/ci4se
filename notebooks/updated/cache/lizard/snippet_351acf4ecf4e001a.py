def read_ssh_config(path):
    with open(path, 'r') as fh_:
        lines = fh_.read().splitlines()
    return SshConfig(lines)