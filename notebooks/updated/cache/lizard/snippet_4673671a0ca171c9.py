def bind(self, instance):
    p = self.clone()
    p.instance = weakref.ref(instance)
    return p