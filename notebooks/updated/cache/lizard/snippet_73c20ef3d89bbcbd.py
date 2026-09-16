def as_view(cls, action_map=None, **initkwargs):
    if not action_map:
        raise TypeError('action_map is a required argument.')

    def view(request):
        self = cls(**initkwargs)
        self.request = request
        self.lookup_url_kwargs = self.request.matchdict
        self.action_map = action_map
        self.action = self.action_map.get(self.request.method.lower())
        for method, action in action_map.items():
            handler = getattr(self, action)
            setattr(self, method, handler)
        return self.dispatch(self.request, **self.request.matchdict)
    return view