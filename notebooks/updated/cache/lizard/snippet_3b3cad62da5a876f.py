def run_hooks(self, name, event=None, context=None):
    hooks = {'pre:setup': lambda p: p.pre_setup(self), 'post:setup': lambda
        p: p.post_setup(self), 'pre:invoke': lambda p: p.pre_invoke(event,
        context), 'post:invoke': lambda p: p.post_invoke(event, context),
        'pre:report': lambda p: p.pre_report(self.report), 'post:report': 
        lambda p: p.post_report(self.report)}
    if name in hooks:
        for p in self.plugins:
            if p.enabled:
                try:
                    hooks[name](p)
                except Exception as e:
                    logger.error('IOpipe plugin %s hook raised error' % (
                        name, str(e)))
                    logger.exception(e)