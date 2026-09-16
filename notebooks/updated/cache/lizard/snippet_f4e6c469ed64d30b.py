def get_instance(self, payload):
    return KeyInstance(self._version, payload, account_sid=self._solution[
        'account_sid'])