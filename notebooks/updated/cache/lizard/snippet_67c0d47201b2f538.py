def create(self, to, channel, custom_message=values.unset, send_digits=
    values.unset, locale=values.unset, custom_code=values.unset, amount=
    values.unset, payee=values.unset):
    data = values.of({'To': to, 'Channel': channel, 'CustomMessage':
        custom_message, 'SendDigits': send_digits, 'Locale': locale,
        'CustomCode': custom_code, 'Amount': amount, 'Payee': payee})
    payload = self._version.create('POST', self._uri, data=data)
    return VerificationInstance(self._version, payload, service_sid=self.
        _solution['service_sid'])