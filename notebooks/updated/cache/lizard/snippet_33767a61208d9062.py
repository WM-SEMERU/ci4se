def get(self, resource='', rid=None, **query):
    if rid:
        if resource[-1] != '/':
            resource += '/'
        resource += str(rid)
    response = self._run_method('GET', resource, query=query)
    return self._handle_response(resource, response)