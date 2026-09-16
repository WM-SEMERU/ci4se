def apply(self, folder):
    logger.info('Apply Patch %s@%s (commit %s)', self.url, self.branch,
        self.commit)
    remote_name = 'patch'
    commands = ['git remote add {} {}'.format(remote_name, self.url),
        'git fetch {} {}'.format(remote_name, self.branch),
        'git merge {} -m "patch"'.format(self.commit),
        'git remote remove {}'.format(remote_name)]
    for command in commands:
        return_code, stream_data = _run_command_inside_folder(command, folder)
        if return_code:
            msg = 'Could not apply patch from {}@{}: {}. Error: {}'.format(self
                .url, self.branch, command, stream_data)
            logger.error(msg)
            raise RuntimeError(msg)