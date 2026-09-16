def retry(self, work_spec_name, *work_unit_names):
    with self.registry.lock(identifier=self.worker_id) as session:
        units = {}
        for work_unit_name in work_unit_names:
            unit = session.get(WORK_UNITS_ + work_spec_name + _FAILED,
                work_unit_name)
            if unit is None:
                spec = session.get(WORK_SPECS, work_spec_name)
                if spec is None:
                    raise NoSuchWorkSpecError(work_spec_name)
                else:
                    raise NoSuchWorkUnitError(work_unit_name)
            if 'traceback' in unit:
                del unit['traceback']
            units[work_unit_name] = unit
        session.move(WORK_UNITS_ + work_spec_name + _FAILED, WORK_UNITS_ +
            work_spec_name, units, priority=0)