def delete_job(self, job_name):
    logger.debug('Deleting job {0}'.format(job_name))
    for idx, job in enumerate(self.jobs):
        if job.name == job_name:
            self.backend.delete_job(job.job_id)
            del self.jobs[idx]
            self.commit()
            return
    raise DagobahError('no job with name %s exists' % job_name)