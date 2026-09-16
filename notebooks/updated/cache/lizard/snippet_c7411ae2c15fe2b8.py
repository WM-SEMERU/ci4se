def enqueue_jobs(self, jobs: Iterable[Job]):
    jobs_to_queue = list()
    for job in jobs:
        if job.should_start:
            job.status = JobStatus.QUEUED
        else:
            job.status = JobStatus.WAITING
        jobs_to_queue.append(job.serialize())
    if jobs_to_queue:
        self._run_script(self._enqueue_job, self._to_namespaced(
            NOTIFICATIONS_KEY), self._to_namespaced(RUNNING_JOBS_KEY.format
            (self._id)), self.namespace, self._to_namespaced(
            FUTURE_JOBS_KEY), *jobs_to_queue)