def register_eph_task(self, *args, **kwargs):
    kwargs['task_class'] = EphTask
    return self.register_task(*args, **kwargs)