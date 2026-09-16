def post_process_response_headers(self, dct):
    if not self.response_headers:
        return
    for key, value in self.response_headers.items():
        parts = key.split('-')
        if len(parts) != 3:
            continue
        if parts[0] != 'X':
            continue
        if parts[-1] != 'Id':
            continue
        dct['{}_id'.format(underscore(parts[1]))] = value