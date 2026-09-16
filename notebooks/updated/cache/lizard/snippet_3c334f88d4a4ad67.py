def chat_post_message(self, channel, text, **params):
    method = 'chat.postMessage'
    params.update({'channel': channel, 'text': text})
    return self._make_request(method, params)