def say(self, text):
    params = {'input': text, 'key': self.key, 'cs': self.cs,
        'conversation_id': self.convo_id, 'wrapper': 'CleverWrap.py'}
    reply = self._send(params)
    self._process_reply(reply)
    return self.output