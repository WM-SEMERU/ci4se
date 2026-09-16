def _stream(self, doc, source, new_data, rollover=None, setter=None):
    old = self._saved_copy()
    for k, v in new_data.items():
        if isinstance(self[k], np.ndarray) or isinstance(new_data[k], np.
            ndarray):
            data = np.append(self[k], new_data[k])
            if rollover and len(data) > rollover:
                data = data[-rollover:]
            super(PropertyValueDict, self).__setitem__(k, data)
        else:
            L = self[k]
            L.extend(new_data[k])
            if rollover is not None:
                del L[:-rollover]
    from ...document.events import ColumnsStreamedEvent
    self._notify_owners(old, hint=ColumnsStreamedEvent(doc, source,
        new_data, rollover, setter))