def delete_direct(self, addresses):
    with self._lock:
        for address in addresses:
            self._validate_write(address)
            if address in self._state:
                self._state[address].set_deleted()
            else:
                fut = _ContextFuture(address=address)
                self._state[address] = fut
                fut.set_deleted()