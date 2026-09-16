def get_inputs(self):
    self.request(EP_GET_INPUTS)
    return {} if self.last_response is None else self.last_response.get(
        'payload').get('devices')