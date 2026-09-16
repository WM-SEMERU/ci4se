def write(self, bytestring):
    with self._lock:
        if self._closed:
            raise IOError('Writer is closed')
        self._byte_queue.put(bytestring)