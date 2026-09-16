def create(self, code, to=values.unset, verification_sid=values.unset,
    amount=values.unset, payee=values.unset):
    data = values.of({'Code': code, 'To': to, 'VerificationSid':
        verification_sid, 'Amount': amount, 'Payee': payee})
    payload = self._version.create('POST', self._uri, data=data)
    return VerificationCheckInstance(self._version, payload, service_sid=
        self._solution['service_sid'])