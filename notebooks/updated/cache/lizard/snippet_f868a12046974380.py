def _get_headers(self, resource):
    if type(resource) == file:
        resource.seek(0)
        reader = csv.reader(resource)
    elif isinstance(resource, basestring):
        result = six.moves.urllib.parse.urlparse(resource)
        if result.scheme in ['http', 'https']:
            with closing(requests.get(resource, stream=True)) as response:
                header_row = response.iter_lines().next()
        else:
            with open(resource) as resource_file:
                reader = csv.reader(resource_file)
                header_row = reader.next()
        reader = csv.reader(cStringIO.StringIO(header_row))
    else:
        raise IOError('Resource type not supported')
    return reader.next()