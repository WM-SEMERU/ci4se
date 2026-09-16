def get_job(self, job_name):
    for job in self.jobs:
        if job.name == job_name:
            return job
    logger.warn('Tried to find job with name {0}, but job not found'.format
        (job_name))
    return None