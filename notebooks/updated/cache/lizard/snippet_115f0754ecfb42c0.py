def do_HEAD(self):
    self.do_initial_operations()
    coap_response = self.client.get(self.coap_uri.path)
    self.client.stop()
    logger.info('Server response: %s', coap_response.pretty_print())
    self.set_http_header(coap_response)