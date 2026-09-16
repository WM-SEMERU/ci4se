def confirm_redirect_uri(self, client_id, code, redirect_uri, client,
    request, *args, **kwargs):
    raise NotImplementedError('Subclasses must implement this method.')