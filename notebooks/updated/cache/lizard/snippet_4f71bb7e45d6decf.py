def reset(self):
    self._reset_ptr[0] = True
    self._commands.clear()
    for _ in range(self._pre_start_steps + 1):
        self.tick()
    return self._default_state_fn()