def get(self, sid):
    return ReservationContext(self._version, workspace_sid=self._solution[
        'workspace_sid'], task_sid=self._solution['task_sid'], sid=sid)