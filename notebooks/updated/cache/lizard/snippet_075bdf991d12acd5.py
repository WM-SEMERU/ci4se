def callback(self, request, **kwargs):
    if self.oauth == 'oauth1':
        token = self.callback_oauth1(request, **kwargs)
    else:
        token = self.callback_oauth2(request)
    service_name = ServicesActivated.objects.get(name=self.service)
    UserService.objects.filter(user=request.user, name=service_name).update(
        token=token)
    back = self.service.split('Service')[1].lower()
    back_to = '{back_to}/callback.html'.format(back_to=back)
    return back_to