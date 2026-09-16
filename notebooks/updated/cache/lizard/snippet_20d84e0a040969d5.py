def generation(self):
    with self._lock:
        if self.state is not MemberState.STABLE:
            return None
        return self._generation