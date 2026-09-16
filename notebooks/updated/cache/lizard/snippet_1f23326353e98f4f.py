def check_startup_state_changed(self):
    ready = self.pg_isready()
    if ready == STATE_REJECT:
        return False
    elif ready == STATE_NO_RESPONSE:
        self.set_state('start failed')
        self._schedule_load_slots = False
        if not self._running_custom_bootstrap:
            self.save_configuration_files()
        return True
    else:
        if ready != STATE_RUNNING:
            logger.warning('%s status returned from pg_isready', 'Unknown' if
                ready == STATE_UNKNOWN else 'Invalid')
        self.set_state('running')
        self._schedule_load_slots = self.use_slots
        if not self._running_custom_bootstrap:
            self.save_configuration_files()
        action = self.__cb_pending or ACTION_ON_START
        self.call_nowait(action)
        self.__cb_pending = None
        return True