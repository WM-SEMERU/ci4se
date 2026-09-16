def create_runscript(self, default='/bin/bash', force=False):
    entrypoint = default
    if force is False:
        if self.entrypoint is not None:
            entrypoint = ''.join(self.entrypoint)
        elif self.cmd is not None:
            entrypoint = ''.join(self.cmd)
    if not entrypoint.startswith('exec'):
        entrypoint = 'exec %s' % entrypoint
    if not re.search('"?[$]@"?', entrypoint):
        entrypoint = '%s "$@"' % entrypoint
    return entrypoint