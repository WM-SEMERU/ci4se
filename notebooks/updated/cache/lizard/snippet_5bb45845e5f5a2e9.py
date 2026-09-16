def get_request_fields(self):
    if hasattr(self, '_request_fields'):
        return self._request_fields
    include_fields = self.get_request_feature(self.INCLUDE)
    exclude_fields = self.get_request_feature(self.EXCLUDE)
    request_fields = {}
    for fields, include in ((include_fields, True), (exclude_fields, False)):
        if fields is None:
            continue
        for field in fields:
            field_segments = field.split('.')
            num_segments = len(field_segments)
            current_fields = request_fields
            for i, segment in enumerate(field_segments):
                last = i == num_segments - 1
                if segment:
                    if last:
                        current_fields[segment] = include
                    else:
                        if segment not in current_fields:
                            current_fields[segment] = {}
                        current_fields = current_fields[segment]
                elif not last:
                    raise exceptions.ParseError(
                        '"%s" is not a valid field.' % field)
    self._request_fields = request_fields
    return request_fields