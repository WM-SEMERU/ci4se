def register_cls_list(self, cls_and_handler):
    for cls, handler in cls_and_handler:
        self._single_dispatch.register(cls, handler)
    self.dispatch.cache_clear()