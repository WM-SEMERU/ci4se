def submit(self, job_id, directory, script=None):
    if job_id is None:
        job_id = '%s_%s_%s' % (Path(directory).unicodename, self.
            destination['username'], make_unique_name())
    else:
        check_jobid(job_id)
    queue = self._get_queue()
    if queue is None:
        queue = self._setup()
    if script is None:
        script = 'start.sh'
    ret, target = self._call('%s %s' % (shell_escape(queue /
        'commands/new_job'), job_id), True)
    if ret == 4:
        raise JobAlreadyExists
    elif ret != 0:
        raise JobNotFound("Couldn't create job")
    target = PosixPath(target)
    logger.debug('Server created directory %s', target)
    try:
        scp_client = self.get_scp_client()
        scp_client.put(str(Path(directory)), str(target), recursive=True)
    except BaseException as e:
        try:
            self.delete(job_id)
        except BaseException:
            raise e
        raise
    logger.debug('Files uploaded')
    self.check_call('%s %s %s %s' % (shell_escape(queue / 'commands/submit'
        ), job_id, shell_escape(target), shell_escape(script)))
    logger.info('Submitted job %s', job_id)
    return job_id