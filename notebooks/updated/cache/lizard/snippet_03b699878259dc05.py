def update(self, role_sid=values.unset, last_consumed_message_index=values.
    unset):
    data = values.of({'RoleSid': role_sid, 'LastConsumedMessageIndex':
        last_consumed_message_index})
    payload = self._version.update('POST', self._uri, data=data)
    return MemberInstance(self._version, payload, service_sid=self.
        _solution['service_sid'], channel_sid=self._solution['channel_sid'],
        sid=self._solution['sid'])