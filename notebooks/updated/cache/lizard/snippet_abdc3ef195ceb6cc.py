def reset(self):
    if self._task_vars is None:
        self._reset_find_task_vars()
    if self._play_context.remote_addr is None:
        raise ansible.errors.AnsibleConnectionFailure(self.reset_compat_msg)
    self._connect()
    self._mitogen_reset(mode='reset')
    self._shutdown_broker()