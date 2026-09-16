def get(self, sid):
    return PayloadContext(self._version, account_sid=self._solution[
        'account_sid'], reference_sid=self._solution['reference_sid'],
        add_on_result_sid=self._solution['add_on_result_sid'], sid=sid)