def _proxy(self):
    if self._context is None:
        self._context = FieldContext(self._version, assistant_sid=self.
            _solution['assistant_sid'], task_sid=self._solution['task_sid'],
            sid=self._solution['sid'])
    return self._context