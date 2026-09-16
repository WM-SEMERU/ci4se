def handle_get_request(self):
    self.objects = self.get_objects()
    self.response = self.get_response_handler()
    self.response.process(self.objects)
    return self.list_response()