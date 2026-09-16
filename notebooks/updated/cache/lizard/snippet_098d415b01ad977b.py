def get_messages(self, folderid='', stack=1, cursor=''):
    if self.standard_grant_type is not 'authorization_code':
        raise DeviantartError(
            'Authentication through Authorization Code (Grant Type) is required in order to connect to this endpoint.'
            )
    response = self._req('/messages/feed', {'folderid': folderid, 'stack':
        stack, 'cursor': cursor})
    messages = []
    for item in response['results']:
        m = Message()
        m.from_dict(item)
        messages.append(m)
    return {'results': messages, 'has_more': response['has_more'], 'cursor':
        response['cursor']}