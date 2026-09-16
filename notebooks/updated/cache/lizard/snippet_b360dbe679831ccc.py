def skip_job(self, job_record):
    original_job_state = job_record.state
    if not job_record.is_finished:
        job_record.state = job.STATE_SKIPPED
        self.job_dao.update(job_record)
    if job_record.related_unit_of_work:
        uow = self.uow_dao.get_one(job_record.related_unit_of_work)
        if not uow.is_finished:
            uow.state = unit_of_work.STATE_CANCELED
            uow.submitted_at = datetime.utcnow()
            self.uow_dao.update(uow)
    msg = 'Skipped Job {0} for {1}@{2}: state transfer {3} -> {4};'.format(
        job_record.db_id, job_record.process_name, job_record.timeperiod,
        original_job_state, job_record.state)
    self._log_message(WARNING, job_record.process_name, job_record.
        timeperiod, msg)