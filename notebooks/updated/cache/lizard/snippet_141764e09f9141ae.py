def open_read(self, headers=None, query_args='', override_num_retries=None,
    response_headers=None):
    if self.resp == None:
        self.mode = 'r'
        provider = self.bucket.connection.provider
        self.resp = self.bucket.connection.make_request('GET', self.bucket.
            name, self.name, headers, query_args=query_args,
            override_num_retries=override_num_retries)
        if self.resp.status < 199 or self.resp.status > 299:
            body = self.resp.read()
            raise provider.storage_response_error(self.resp.status, self.
                resp.reason, body)
        response_headers = self.resp.msg
        self.metadata = boto.utils.get_aws_metadata(response_headers, provider)
        for name, value in response_headers.items():
            if name.lower(
                ) == 'content-length' and 'Content-Range' not in response_headers:
                self.size = int(value)
            elif name.lower() == 'content-range':
                end_range = re.sub('.*/(.*)', '\\1', value)
                self.size = int(end_range)
            elif name.lower() == 'etag':
                self.etag = value
            elif name.lower() == 'content-type':
                self.content_type = value
            elif name.lower() == 'content-encoding':
                self.content_encoding = value
            elif name.lower() == 'last-modified':
                self.last_modified = value
            elif name.lower() == 'cache-control':
                self.cache_control = value
        self.handle_version_headers(self.resp)
        self.handle_encryption_headers(self.resp)