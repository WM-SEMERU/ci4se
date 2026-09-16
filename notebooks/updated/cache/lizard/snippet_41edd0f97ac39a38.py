def _extract_updater(self):
    if self._node is self._buffer:
        return None
    else:
        updater = self._node, self._buffer
        self._buffer = self._node
        return updater