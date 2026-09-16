def binary(self, url, timeout=None):
    response = self.get_response(url, timeout=timeout)
    if response:
        return response.content
    else:
        return None