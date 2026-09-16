def quick_add(self, api_token, text, **kwargs):
    params = {'token': api_token, 'text': text}
    return self._post('quick/add', params, **kwargs)