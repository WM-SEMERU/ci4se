def send_formdata(self, request, headers=None, content=None, **config):
    request.headers = headers
    request.add_formdata(content)
    return self.send(request, **config)