def get(self, index):
    if self and index <= len(self) - 1:
        return self._result_cache[index]