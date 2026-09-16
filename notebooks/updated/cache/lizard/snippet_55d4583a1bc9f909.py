def wave(self, wave_first=True, thread_id=None, thread_type=None):
    thread_id, thread_type = self._getThread(thread_id, thread_type)
    data = self._getSendData(thread_id=thread_id, thread_type=thread_type)
    data['action_type'] = 'ma-type:user-generated-message'
    data['lightweight_action_attachment[lwa_state]'
        ] = 'INITIATED' if wave_first else 'RECIPROCATED'
    data['lightweight_action_attachment[lwa_type]'] = 'WAVE'
    if thread_type == ThreadType.USER:
        data['specific_to_list[0]'] = 'fbid:{}'.format(thread_id)
    return self._doSendRequest(data)