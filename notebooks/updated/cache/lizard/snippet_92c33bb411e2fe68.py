def _head(self, client_kwargs):
    with _handle_client_exception():
        if 'obj' in client_kwargs:
            return self.client.head_object(**client_kwargs)
        return self.client.head_container(**client_kwargs)