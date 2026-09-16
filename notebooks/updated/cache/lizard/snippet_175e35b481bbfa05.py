def run(self):
    region = AWSServiceRegion(access_key=self.key, secret_key=self.secret,
        uri=self.endpoint)
    query = self.query_factory(action=self.action, creds=region.creds,
        endpoint=region.ec2_endpoint, other_params=self.parameters)

    def write_response(response):
        print >> self.output, 'URL: %s' % query.client.url
        print >> self.output
        print >> self.output, 'HTTP status code: %s' % query.client.status
        print >> self.output
        print >> self.output, response

    def write_error(failure):
        if failure.check(AWSError):
            message = failure.value.original
        else:
            message = failure.getErrorMessage()
            if message.startswith('Error Message: '):
                message = message[len('Error Message: '):]
        print >> self.output, 'URL: %s' % query.client.url
        print >> self.output
        if getattr(query.client, 'status', None) is not None:
            print >> self.output, 'HTTP status code: %s' % (query.client.
                status,)
            print >> self.output
        print >> self.output, message
        if getattr(failure.value, 'response', None) is not None:
            print >> self.output
            print >> self.output, failure.value.response
    deferred = query.submit()
    deferred.addCallback(write_response)
    deferred.addErrback(write_error)
    return deferred