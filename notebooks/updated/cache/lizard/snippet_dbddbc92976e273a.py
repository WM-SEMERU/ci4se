def response_delay(self, delay):
    if isinstance(delay, (int, float)) and delay >= 0 or delay is None:
        self._response_delay = delay
    else:
        raise ValueError(_format(
            'Invalid value for response_delay: {0!A}, must be a positive number'
            , delay))