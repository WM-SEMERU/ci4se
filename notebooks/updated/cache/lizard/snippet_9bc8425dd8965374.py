def build(self):
    for cmd in self.build_cmds:
        log.info('building command: {}'.format(cmd))
        full_cmd = 'cd {}; {}'.format(self.analyses_path, cmd)
        log.debug('full command: {}'.format(full_cmd))
        subprocess.call(full_cmd, shell=True)
        log.info('build done')