def parse(self, request):
    if request.method in ('POST', 'PUT', 'PATCH'):
        content_type = self.determine_content(request)
        if content_type:
            split = content_type.split(';', 1)
            if len(split) > 1:
                content_type = split[0]
            content_type = content_type.strip()
        parser = self._meta.parsers_dict.get(content_type, self._meta.
            default_parser)
        data = parser(self).parse(request)
        return dict() if isinstance(data, basestring) else data
    return dict()