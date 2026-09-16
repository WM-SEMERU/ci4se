def get_instance(self, payload):
    return TranscriptionInstance(self._version, payload, account_sid=self.
        _solution['account_sid'], recording_sid=self._solution['recording_sid']
        )