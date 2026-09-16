def make_middleware(self, app):

    def application(environ, start_response):
        return ClosingIterator(app(environ, start_response), self.cleanup)
    return application