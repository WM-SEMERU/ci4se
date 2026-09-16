def create(self, email, tos=1, options=None):
    data = {'email': email, 'terms_of_service': str(tos)}
    if options:
        data.update(options)
    return self.post(self.base_url, body=json.dumps(data))