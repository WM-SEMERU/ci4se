def get_events(self):
    result = []
    while self._wait(0):
        event = self._read()
        if event:
            result.append(event)
    return result