def create(self, friendly_name, api_version=values.unset, voice_url=values.
    unset, voice_method=values.unset, voice_fallback_url=values.unset,
    voice_fallback_method=values.unset, status_callback=values.unset,
    status_callback_method=values.unset, voice_caller_id_lookup=values.
    unset, sms_url=values.unset, sms_method=values.unset, sms_fallback_url=
    values.unset, sms_fallback_method=values.unset, sms_status_callback=
    values.unset, message_status_callback=values.unset):
    data = values.of({'FriendlyName': friendly_name, 'ApiVersion':
        api_version, 'VoiceUrl': voice_url, 'VoiceMethod': voice_method,
        'VoiceFallbackUrl': voice_fallback_url, 'VoiceFallbackMethod':
        voice_fallback_method, 'StatusCallback': status_callback,
        'StatusCallbackMethod': status_callback_method,
        'VoiceCallerIdLookup': voice_caller_id_lookup, 'SmsUrl': sms_url,
        'SmsMethod': sms_method, 'SmsFallbackUrl': sms_fallback_url,
        'SmsFallbackMethod': sms_fallback_method, 'SmsStatusCallback':
        sms_status_callback, 'MessageStatusCallback': message_status_callback})
    payload = self._version.create('POST', self._uri, data=data)
    return ApplicationInstance(self._version, payload, account_sid=self.
        _solution['account_sid'])