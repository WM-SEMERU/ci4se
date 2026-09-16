def process_request_thread(self, request, client_address):
    try:
        self.finish_request(request, client_address)
        self.shutdown_request(request)
    except Exception as e:
        self.logger.error(e)
        self.handle_error(request, client_address)
        self.shutdown_request(request)