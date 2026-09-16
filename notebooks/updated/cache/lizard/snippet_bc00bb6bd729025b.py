def mustExposeRequest(self, service_request):
    expose_request = service_request.service.mustExposeRequest(service_request)
    if expose_request is None:
        if self.expose_request is None:
            return False
        return self.expose_request
    return expose_request