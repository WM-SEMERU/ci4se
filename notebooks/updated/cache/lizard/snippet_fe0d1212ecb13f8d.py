def get_jobs(self, job_ids=None):
    if job_ids is not None and len(job_ids) == 0:
        return []
    q = self.session.query(Job)
    if job_ids is not None:
        q = q.filter(Job.unique.in_(job_ids))
    return sorted(list(q), key=lambda job: job.unique)