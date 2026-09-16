def expanduser(self, filepath, ssh=False):
    if ssh:
        self._check_ssh()
        stdin, stdout, stderr = self.ssh.exec_command('cd; pwd')
        stdin.close()
        remotepath = filepath.replace('~', stdout.read().split()[0])
        return self._get_tramp_path(remotepath)
    else:
        return os.path.expanduser(filepath)