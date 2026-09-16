def process_kwargs(self, kwargs, prefix='default_', delete=True):
    processed = []
    for k in kwargs:
        if hasattr(self, prefix + k):
            processed += [k]
            setattr(self, prefix + k, kwargs[k])
    for k in processed:
        del kwargs[k]
    return kwargs