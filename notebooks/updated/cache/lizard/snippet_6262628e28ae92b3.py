def process_response(self, request, response):
    if hasattr(threadlocal, 'auditlog'):
        pre_save.disconnect(sender=LogEntry, dispatch_uid=threadlocal.
            auditlog['signal_duid'])
    return response