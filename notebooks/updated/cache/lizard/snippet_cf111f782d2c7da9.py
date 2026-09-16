def sendVideoNote(self, chat_id, video_note, duration=None, length=None,
    disable_notification=None, reply_to_message_id=None, reply_markup=None):
    p = _strip(locals(), more=['video_note'])
    return self._api_request_with_file('sendVideoNote', _rectify(p),
        'video_note', video_note)