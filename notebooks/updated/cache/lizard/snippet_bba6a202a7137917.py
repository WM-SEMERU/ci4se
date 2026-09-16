def _getPayload(self, record):
    try:
        d = record.__dict__
        pid = d.pop('process', 'nopid')
        tid = d.pop('thread', 'notid')
        payload = {k: v for k, v in d.items() if k in TOP_KEYS}
        payload['meta'] = {k: v for k, v in d.items() if k in META_KEYS}
        payload['details'] = {k: simple_json(v) for k, v in d.items() if k
             not in self.detail_ignore_set}
        payload['log'] = payload.pop('name', 'n/a')
        payload['level'] = payload.pop('levelname', 'n/a')
        payload['meta']['line'] = payload['meta'].pop('lineno', 'n/a')
        payload['message'] = record.getMessage()
        tb = self._getTraceback(record)
        if tb:
            payload['traceback'] = tb
    except Exception as e:
        payload = {'level': 'ERROR', 'message': 'could not format',
            'exception': repr(e)}
    payload['pid'] = 'p-{}'.format(pid)
    payload['tid'] = 't-{}'.format(tid)
    return payload