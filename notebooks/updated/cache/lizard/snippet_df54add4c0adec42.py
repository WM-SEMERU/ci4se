def wait_for_compilation_job(self, job, poll=5):
    desc = _wait_until(lambda : _compilation_job_status(self.
        sagemaker_client, job), poll)
    self._check_job_status(job, desc, 'CompilationJobStatus')
    return desc