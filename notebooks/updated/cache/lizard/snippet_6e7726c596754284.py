def _setup(self):
    if self.queue.path[0:1] == b'/':
        queue = self.queue
    else:
        if self.queue.path[0:1] == b'~':
            output = self.check_output('echo %s' % escape_queue(self.queue))
            queue = PosixPath(output.rstrip(b'\r\n'))
        else:
            output = self.check_output('pwd')
            queue = PosixPath(output.rstrip(b'\r\n')) / self.queue
        logger.debug('Resolved to %s', queue)
    if not self.setup_runtime:
        if self._call('which qsub', False)[0] == 0:
            logger.debug("qsub is available, using runtime 'pbs'")
            runtime = 'pbs'
        else:
            logger.debug("qsub not found, using runtime 'default'")
            runtime = 'default'
    else:
        runtime = self.setup_runtime
    if self.need_runtime is not None and runtime not in self.need_runtime:
        raise ValueError(
            "About to setup runtime %s but that wouldn't match explicitely allowed runtimes"
             % runtime)
    logger.info('Installing runtime %s%s at %s', runtime, '' if self.
        setup_runtime else ' (auto)', self.queue)
    scp_client = self.get_scp_client()
    filename = pkg_resources.resource_filename('tej', 'remotes/%s' % runtime)
    scp_client.put(filename, str(queue), recursive=True)
    logger.debug('Files uploaded')
    self.check_call('/bin/sh %s' % shell_escape(queue / 'commands/setup'))
    logger.debug('Post-setup script done')
    self._queue = queue
    return queue