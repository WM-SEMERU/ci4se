def _sendFiles(self, files, message=None, thread_id=None, thread_type=
    ThreadType.USER):
    thread_id, thread_type = self._getThread(thread_id, thread_type)
    data = self._getSendData(message=self._oldMessage(message), thread_id=
        thread_id, thread_type=thread_type)
    data['action_type'] = 'ma-type:user-generated-message'
    data['has_attachment'] = True
    for i, (file_id, mimetype) in enumerate(files):
        data['{}s[{}]'.format(mimetype_to_key(mimetype), i)] = file_id
    return self._doSendRequest(data)