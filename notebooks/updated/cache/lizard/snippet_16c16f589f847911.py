def lookup_rest_method(self, orig_request):
    method_name, method, params = self.config_manager.lookup_rest_method(
        orig_request.path, orig_request.request_uri, orig_request.http_method)
    orig_request.method_name = method_name
    return method, params