def build(self, **kwargs):
    resp = self.client.api.build(**kwargs)
    if isinstance(resp, six.string_types):
        return self.get(resp)
    last_event = None
    image_id = None
    result_stream, internal_stream = itertools.tee(json_stream(resp))
    for chunk in internal_stream:
        if 'error' in chunk:
            raise BuildError(chunk['error'], result_stream)
        if 'stream' in chunk:
            match = re.search('(^Successfully built |sha256:)([0-9a-f]+)$',
                chunk['stream'])
            if match:
                image_id = match.group(2)
        last_event = chunk
    if image_id:
        return self.get(image_id), result_stream
    raise BuildError(last_event or 'Unknown', result_stream)