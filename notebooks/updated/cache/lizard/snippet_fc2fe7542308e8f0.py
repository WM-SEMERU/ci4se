def manage_schedulable(self, freerun_entry, flow_request=None):
    assert isinstance(freerun_entry, FreerunProcessEntry)
    uow = None
    if freerun_entry.related_unit_of_work:
        uow = self.uow_dao.get_one(freerun_entry.related_unit_of_work)
    try:
        if uow is None:
            self._process_state_embryo(freerun_entry, flow_request)
        elif uow.is_requested or uow.is_in_progress:
            self._process_state_in_progress(freerun_entry, uow)
        elif uow.is_finished or uow.is_invalid:
            self._process_terminal_state(freerun_entry, uow, flow_request)
        else:
            msg = 'Unknown state {0} of the UOW {1}'.format(uow.state, uow.
                db_id)
            self._log_message(ERROR, freerun_entry, msg)
    except LookupError as e:
        msg = (
            'Lookup issue for schedulable: {0} in timeperiod {1}, because of: {2}'
            .format(freerun_entry.db_id, uow.timeperiod, e))
        self._log_message(WARNING, freerun_entry, msg)