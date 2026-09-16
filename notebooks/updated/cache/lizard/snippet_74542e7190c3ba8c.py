def sh(self, cmd, ignore_error=False, cwd=None, shell=False, **kwargs):
    kwargs.update({'shell': shell, 'cwd': cwd or self.fpath, 'stderr':
        subprocess.STDOUT, 'stdout': subprocess.PIPE, 'ignore_error':
        ignore_error})
    log.debug((('cmd', cmd), ('kwargs', kwargs)))
    return sh(cmd, **kwargs)