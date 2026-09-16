def get_resource(self):
    return Resource(self.rest_client.make_request(self.resource), self.
        rest_client)