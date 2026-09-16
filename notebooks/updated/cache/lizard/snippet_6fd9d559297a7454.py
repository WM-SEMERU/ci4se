def _parse_view_results(self, rows, factory, options):
    kwargs = dict()
    kwargs['reduced'] = factory.use_reduce and options.get('reduce', True)
    kwargs['include_docs'] = options.get('include_docs', False)
    spec = inspect.getargspec(factory.parse_view_result)
    if 'unserialize' in spec.args:
        kwargs['unserialize'] = self.unserialize_document
    if 'unserialize_list' in spec.args:
        kwargs['unserialize_list'] = self.unserialize_list_of_documents
    return factory.parse_view_result(rows, **kwargs)