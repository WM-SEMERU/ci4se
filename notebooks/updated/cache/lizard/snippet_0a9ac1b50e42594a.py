def cancel(self, job_ids):
    for job_id in job_ids:
        try:
            self.deployer.destroy(self.resources.get(job_id))
            return True
        except e:
            logger.error('Failed to cancel {}'.format(repr(job_id)))
            logger.error(e)
            return False