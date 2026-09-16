def _GetDebuggeeDescription(self):
    return '-'.join(self._debuggee_labels[label] for label in
        _DESCRIPTION_LABELS if label in self._debuggee_labels)