def get(self, sid):
    return TaskContext(self._version, assistant_sid=self._solution[
        'assistant_sid'], sid=sid)