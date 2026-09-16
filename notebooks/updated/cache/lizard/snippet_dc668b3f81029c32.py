def _process_request(self, request, client_address):
    try:
        self.finish_request(request, client_address)
    except Exception:
        self.handle_error(request, client_address)
    finally:
        self.shutdown_request(request)