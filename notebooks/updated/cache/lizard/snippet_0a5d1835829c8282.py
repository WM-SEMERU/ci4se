def handle_provider(self, provider_factory, note):
    basenote, name = self.parse_note(note)
    if basenote not in self.instances:
        if isinstance(provider_factory, type) and self.has_annotations(
            provider_factory.__init__):
            args, kwargs = self.prepare_callable(provider_factory.__init__)
            self.instances[basenote] = provider_factory(*args, **kwargs)
        else:
            self.instances[basenote] = self.apply_regardless(provider_factory)
        provider = self.instances[basenote]
        if hasattr(provider, 'close'):
            self.finalizers.append(self.instances[basenote].close)
    provider = self.instances[basenote]
    get = self.partial_regardless(provider.get)
    try:
        if name is not None:
            return get(name=name)
        self.values[basenote] = get()
        return self.values[basenote]
    except UnsetError:
        exc_type, exc_value, tb = sys.exc_info()
        exc_msg = str(exc_value)
        if exc_msg:
            msg = '{}: {!r}'.format(exc_msg, note)
        else:
            msg = repr(note)
        six.reraise(exc_type, exc_type(msg, note=note), tb)