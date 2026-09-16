def _make_dir(self, client_kwargs):
    with _handle_azure_exception():
        if 'directory_name' in client_kwargs:
            return self.client.create_directory(share_name=client_kwargs[
                'share_name'], directory_name=client_kwargs['directory_name'])
        return self.client.create_share(**client_kwargs)