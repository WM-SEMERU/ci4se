def register(self, prefix, viewset, base_name=None, router_class=None):
    if base_name is None:
        base_name = self.get_default_base_name(viewset)
    if router_class is not None:
        kwargs = {'trailing_slash': bool(self.trailing_slash)}
        single_object_router_classes = AuthenticationRouter, SingleObjectRouter
        if issubclass(router_class, single_object_router_classes):
            router = router_class(**kwargs)
            router.register(prefix, viewset, base_name=base_name)
            self._single_object_registry.append(router)
    else:
        self.registry.append((prefix, viewset, base_name))