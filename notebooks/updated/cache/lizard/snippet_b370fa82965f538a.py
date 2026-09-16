def _do_autopaginating_api_call(self, method, kwargs, parser_func):
    has_records = {'has_records': False}
    while True:
        try:
            root = self._do_api_call(method, kwargs)
        except RecordDoesNotExistError:
            if not has_records['has_records']:
                raise
            return
        records_returned_by_this_loop = False
        for record in parser_func(root, has_records):
            yield record
            records_returned_by_this_loop = True
        if not records_returned_by_this_loop:
            return
        last_offset = root.find('lastOffset').text
        kwargs['offset'] = last_offset