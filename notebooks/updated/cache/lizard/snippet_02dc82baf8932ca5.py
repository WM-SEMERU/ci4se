def delete_notes(self, noteids):
    if self.standard_grant_type is not 'authorization_code':
        raise DeviantartError(
            'Authentication through Authorization Code (Grant Type) is required in order to connect to this endpoint.'
            )
    response = self._req('/notes/delete', post_data={'noteids[]': noteids})
    return response