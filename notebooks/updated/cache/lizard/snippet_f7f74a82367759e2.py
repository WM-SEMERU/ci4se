def open(self, uri, **kwargs):
    handler = self.handler(uri.scheme())
    if handler is None:
        raise WSchemeCollection.NoHandlerFound(uri)
    if uri.scheme() is None:
        uri.component('scheme', handler.scheme_specification().scheme_name())
    if handler.scheme_specification().is_compatible(uri) is False:
        raise WSchemeCollection.SchemeIncompatible(uri)
    return handler.create_handler(uri, **kwargs)