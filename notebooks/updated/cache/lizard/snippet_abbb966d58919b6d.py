def path(self):
    raw_path = wsgi_decoding_dance(self.environ.get('PATH_INFO') or '',
        self.charset, self.encoding_errors)
    return '/' + raw_path.lstrip('/')