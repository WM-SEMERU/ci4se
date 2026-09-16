def execute(self, result=None):
    try:
        return self.unsafe_execute(result=result)
    except Exception as exc:
        return self._onerror(Result.from_exception(exc, uuid=self.uuid))