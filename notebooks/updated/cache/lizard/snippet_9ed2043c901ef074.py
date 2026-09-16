def list_extensions(self):
    r = request.ListExtensions(display=self.display)
    return r.names