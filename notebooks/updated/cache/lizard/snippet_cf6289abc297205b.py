def update_by_function(self, extra_doc, index, doc_type, id,
    querystring_args=None, update_func=None, attempts=2):
    if querystring_args is None:
        querystring_args = {}
    if update_func is None:
        update_func = dict.update
    for attempt in range(attempts - 1, -1, -1):
        current_doc = self.get(index, doc_type, id, **querystring_args)
        new_doc = update_func(current_doc, extra_doc)
        if new_doc is None:
            new_doc = current_doc
        try:
            return self.index(new_doc, index, doc_type, id, version=
                current_doc._meta.version, querystring_args=querystring_args)
        except VersionConflictEngineException:
            if attempt <= 0:
                raise
            self.refresh(index)