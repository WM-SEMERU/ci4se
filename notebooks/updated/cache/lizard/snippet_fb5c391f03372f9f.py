def get(self, request, *args, **kwargs):
    activated_user = self.activate(*args, **kwargs)
    if activated_user:
        users_signals.user_activated.send(sender=self.__class__, user=
            activated_user, request=request)
        return redirect(self.success_url)
    return super().get(request, *args, **kwargs)