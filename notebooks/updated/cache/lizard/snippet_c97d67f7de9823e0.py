def get(self, request, *args, **kwargs):
    response = super(EntryProtectionMixin, self).get(request, *args, **kwargs)
    if self.object.login_required and not request.user.is_authenticated:
        return self.login()
    if (self.object.password and self.object.password != self.request.
        session.get(self.session_key % self.object.pk)):
        return self.password()
    return response