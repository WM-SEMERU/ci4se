def _wait_on_instance(self, state, timeout=600, wait_period=10):
    current_state = 'Undefined'
    start = time.time()
    end = start + timeout
    while time.time() < end:
        current_state = self._get_instance_state()
        if state.lower() == current_state.lower():
            return
        time.sleep(wait_period)
    raise IpaCloudException(
        'Instance has not arrived at the given state: {state}'.format(state
        =state))