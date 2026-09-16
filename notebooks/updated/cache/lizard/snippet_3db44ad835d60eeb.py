def resp_set_location(self, resp, location=None):
    if location:
        self.location = location
    elif resp:
        self.location = resp.label.decode().replace('\x00', '')