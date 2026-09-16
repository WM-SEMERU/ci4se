def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    self.login()
    if self.object.password:
        entry_password = self.request.POST.get('entry_password')
        if entry_password:
            if entry_password == self.object.password:
                self.request.session[self.session_key % self.object.pk
                    ] = self.object.password
                return self.get(request, *args, **kwargs)
            else:
                self.error = True
        return self.password()
    return self.get(request, *args, **kwargs)