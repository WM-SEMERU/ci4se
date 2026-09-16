def schedule_job(self, job):
    l = _reraise_with_traceback(job.get_lambda_to_execute())
    future = self.workers.submit(l, update_progress_func=self.
        update_progress, cancel_job_func=self._check_for_cancel)
    self.job_future_mapping[future] = job
    self.future_job_mapping[job.job_id] = future
    future.add_done_callback(self.handle_finished_future)
    self.cancel_notifications[job.job_id] = False
    return future