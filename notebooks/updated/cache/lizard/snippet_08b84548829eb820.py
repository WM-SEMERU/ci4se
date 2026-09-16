def u2handlers(self):
    return_handlers = suds.transport.http.HttpTransport.u2handlers(self)
    return_handlers.extend(self.handlers)
    return return_handlers