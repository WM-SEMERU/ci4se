def instance_ik_model_receiver(fn):

    @wraps(fn)
    def receiver(self, sender, **kwargs):
        if not inspect.isclass(sender):
            return
        for src in self._source_groups:
            if issubclass(sender, src.model_class):
                fn(self, sender=sender, **kwargs)
                return
    return receiver