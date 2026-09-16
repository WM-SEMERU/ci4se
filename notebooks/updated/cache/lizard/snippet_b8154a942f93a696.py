def post(self, request, *args, **kwargs):
    return self.lock(request, *args, **kwargs)