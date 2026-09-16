def set_redirect(self, url, status=HttpStatusCodes.HTTP_303):
    self.set_status(status)
    self.set_content('')
    self.set_header(HttpResponseHeaders.LOCATION, url)