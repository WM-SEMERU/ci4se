def initial(self, request, *args, **kwargs):
    self.format_kwarg = self.get_format_suffix(**kwargs)
    self.perform_authentication(request)
    self.check_permissions(request)
    self.check_throttles(request)
    neg = self.perform_content_negotiation(request)
    request.accepted_renderer, request.accepted_media_type = neg
    version, scheme = self.determine_version(request, *args, **kwargs)
    request.version, request.versioning_scheme = version, scheme