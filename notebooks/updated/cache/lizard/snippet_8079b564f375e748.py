def get_key(self, args=None, kwargs=None):
    restrict_to = self.once.get('keys', None)
    args = args or {}
    kwargs = kwargs or {}
    call_args = getcallargs(getattr(self, '_orig_run', self.run), *args, **
        kwargs)
    if isinstance(call_args.get('self'), Task):
        del call_args['self']
    key = queue_once_key(self.name, call_args, restrict_to)
    return key