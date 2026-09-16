def process(self, data=None):
    return super(RequestHandler, self).process(data=data or self.
        get_request_data())