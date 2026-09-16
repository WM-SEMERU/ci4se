def get_all_if_deleted(self):
    with self._lock:
        results = {}
        for add, fut in self._state.items():
            if self._contains_and_deleted(add):
                results[add] = fut.result()
        return results