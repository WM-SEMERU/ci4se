def _cleanup_processing_chain(self):
    self.log('Removing stale processing chain entries.')
    self._processing_chain = [x for x in self._processing_chain if x.
        remember_between_connections]