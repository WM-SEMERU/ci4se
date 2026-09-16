def fetch_job(self, job_id, checkout=False):
    self.job_id = job_id
    self.logger.debug('Git fetch job reference %s' % (self.ref_head,))
    out, code, err = self.command_exec(['ls-remote', 'origin', self.ref_head])
    if code:
        self.logger.error('Could not find the job ' + job_id +
            ' on the server. Are you online and does the job exist?')
        sys.exit(1)
    try:
        self.command_exec(['fetch', '-f', '-n', 'origin', self.ref_head +
            ':' + self.ref_head])
    except Exception:
        self.logger.error('Could not load job information for ' + job_id +
            '. You need to be online to start pre-configured jobs.')
        raise
    self.read_job(job_id, checkout)