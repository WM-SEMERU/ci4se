def modify_job(self, id, jobstore=None, **changes):
    fix_job_def(changes)
    if 'trigger' in changes:
        trigger, trigger_args = pop_trigger(changes)
        self._scheduler.reschedule_job(id, jobstore, trigger, **trigger_args)
    return self._scheduler.modify_job(id, jobstore, **changes)