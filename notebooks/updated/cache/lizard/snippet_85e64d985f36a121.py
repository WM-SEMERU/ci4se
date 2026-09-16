def _raiseFindFailed(self, pattern):
    event = FindFailedEvent(self, pattern=pattern, event_type='FINDFAILED')
    if self._findFailedHandler is not None:
        self._findFailedHandler(event)
    response = event._response or self._findFailedResponse
    if response == 'PROMPT':
        response = _findFailedPrompt(pattern)
    if response == 'ABORT':
        raise FindFailed(event)
    elif response == 'SKIP':
        return False
    elif response == 'RETRY':
        return True