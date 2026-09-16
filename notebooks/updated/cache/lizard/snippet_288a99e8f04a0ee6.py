def finish(self, *args, **kwargs):
    log.debug('finish(args={args}, kwargs={kwargs})'.format(args=args,
        kwargs=kwargs))
    self.on_finish(*args, **kwargs)