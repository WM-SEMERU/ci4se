def _listdir(self, path):
    if self._user is None:
        return os.listdir(path)
    else:
        args = self._build_cmdline(['/bin/ls', '-1A', path])
        return subprocess.check_output(args, stderr=DEVNULL).decode('utf-8',
            errors='ignore').split('\n')