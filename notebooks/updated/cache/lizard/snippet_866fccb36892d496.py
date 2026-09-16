def patch(self, patched_value):
    try:
        if self.getter:
            setattr(self.getter_class, self.attr_name, patched_value)
        else:
            setattr(self.orig_object, self.attr_name, patched_value)
    except TypeError:
        proxy_name = 'fudge_proxy_%s_%s_%s' % (self.orig_object.__module__,
            self.orig_object.__name__, patched_value.__class__.__name__)
        self.proxy_object = type(proxy_name, (self.orig_object,), {self.
            attr_name: patched_value})
        mod = sys.modules[self.orig_object.__module__]
        setattr(mod, self.orig_object.__name__, self.proxy_object)