def _insert_uow(self, process_name, timeperiod, start_timeperiod,
    end_timeperiod, start_id, end_id):
    uow = UnitOfWork()
    uow.process_name = process_name
    uow.timeperiod = timeperiod
    uow.start_id = str(start_id)
    uow.end_id = str(end_id)
    uow.start_timeperiod = start_timeperiod
    uow.end_timeperiod = end_timeperiod
    uow.created_at = datetime.utcnow()
    uow.submitted_at = datetime.utcnow()
    uow.source = context.process_context[process_name].source
    uow.sink = context.process_context[process_name].sink
    uow.state = unit_of_work.STATE_REQUESTED
    uow.unit_of_work_type = unit_of_work.TYPE_MANAGED
    uow.number_of_retries = 0
    uow.arguments = context.process_context[process_name].arguments
    uow.db_id = self.uow_dao.insert(uow)
    msg = 'Created: UOW {0} for {1}@{2}.'.format(uow.db_id, process_name,
        start_timeperiod)
    self._log_message(INFO, process_name, start_timeperiod, msg)
    return uow