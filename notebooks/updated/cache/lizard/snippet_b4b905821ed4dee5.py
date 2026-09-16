def _do_log(self, client, _entry_class, payload=None, **kw):
    client = self._require_client(client)
    kw['log_name'] = kw.pop('log_name', self.full_name)
    kw['labels'] = kw.pop('labels', self.labels)
    kw['resource'] = kw.pop('resource', _GLOBAL_RESOURCE)
    if payload is not None:
        entry = _entry_class(payload=payload, **kw)
    else:
        entry = _entry_class(**kw)
    api_repr = entry.to_api_repr()
    client.logging_api.write_entries([api_repr])