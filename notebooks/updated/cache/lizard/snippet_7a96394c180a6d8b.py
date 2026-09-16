def get_coordinates(self, i, end=False):
    if end:
        endpoint = self.endpoints[i][1]
    else:
        endpoint = self.endpoints[i][0]
    return endpoint.real, endpoint.imag