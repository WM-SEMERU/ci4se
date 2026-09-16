def get_work_units(self, work_spec_name, work_unit_keys=None, state=None,
    limit=None, start=None):
    if work_unit_keys is not None:
        raise NotImplementedError('get_work_units(by work_unit_keys)')
    if start is None:
        start = 0
    if state is not None:
        if state == AVAILABLE:
            return self.list_available_work_units(work_spec_name, start=
                start, limit=limit).items()
        if state == PENDING:
            return self.list_pending_work_units(work_spec_name, start=start,
                limit=limit).items()
        if state == BLOCKED:
            return self.list_blocked_work_units(work_spec_name, start=start,
                limit=limit).items()
        if state == FINISHED:
            return self.list_finished_work_units(work_spec_name, start=
                start, limit=limit).items()
        if state == FAILED:
            return self.list_failed_work_units(work_spec_name, start=start,
                limit=limit).items()
        raise ProgrammerError('unknown state {0!r}'.format(state))
    work_units = {}
    work_units.update(self.list_work_units(work_spec_name))
    work_units.update(self.list_blocked_work_units(work_spec_name))
    work_units.update(self.list_finished_work_units(work_spec_name))
    work_units.update(self.list_failed_work_units(work_spec_name))
    return work_units.items()