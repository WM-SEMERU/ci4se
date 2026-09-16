def load_application_key_file(self, filename=b'spotify_appkey.key'):
    with open(filename, 'rb') as fh:
        self.app_key = fh.read()