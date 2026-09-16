def branch(self):
    cmd = ['git', 'symbolic-ref', '--short', 'HEAD']
    try:
        output = self.sh(cmd, shell=False, ignore_error=True).rstrip()
    except subprocess.CalledProcessError as e:
        log.exception(e)
        return '#err# %s' % output
    if output.startswith('fatal: ref HEAD is not a symbolic ref'):
        output = '# %s' % output
    return output