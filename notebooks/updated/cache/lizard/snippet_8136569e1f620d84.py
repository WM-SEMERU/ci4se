def create(self, phone_number, sms_capability, account_sid=values.unset,
    friendly_name=values.unset, unique_name=values.unset, cc_emails=values.
    unset, sms_url=values.unset, sms_method=values.unset, sms_fallback_url=
    values.unset, sms_fallback_method=values.unset, status_callback_url=
    values.unset, status_callback_method=values.unset, sms_application_sid=
    values.unset, address_sid=values.unset, email=values.unset,
    verification_type=values.unset, verification_document_sid=values.unset):
    data = values.of({'PhoneNumber': phone_number, 'SmsCapability':
        sms_capability, 'AccountSid': account_sid, 'FriendlyName':
        friendly_name, 'UniqueName': unique_name, 'CcEmails': serialize.map
        (cc_emails, lambda e: e), 'SmsUrl': sms_url, 'SmsMethod':
        sms_method, 'SmsFallbackUrl': sms_fallback_url, 'SmsFallbackMethod':
        sms_fallback_method, 'StatusCallbackUrl': status_callback_url,
        'StatusCallbackMethod': status_callback_method, 'SmsApplicationSid':
        sms_application_sid, 'AddressSid': address_sid, 'Email': email,
        'VerificationType': verification_type, 'VerificationDocumentSid':
        verification_document_sid})
    payload = self._version.create('POST', self._uri, data=data)
    return HostedNumberOrderInstance(self._version, payload)