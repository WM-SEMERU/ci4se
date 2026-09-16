def _start_watching_events(self, replace=False):
    return self._start_reflector('events', EventReflector, fields={
        'involvedObject.kind': 'Pod'}, replace=replace)