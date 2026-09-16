def get_runtime_config(self, namespace=None):
    namespace = namespace or []
    cfg = getattr(self, 'config', None)
    if cfg is None or not isinstance(cfg, BoundConfig):
        return
    for key, opt in self.get_required_config().options.items():
        yield namespace, key, self.config(key, raise_error=False, raw_value
            =True), opt