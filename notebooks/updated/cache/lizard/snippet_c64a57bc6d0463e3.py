def deny_access(self, request, **kwargs):
    if request.method != 'GET':
        return HttpResponseForbidden()
    message = self.get_access_denied_message(request)
    if message:
        messages.info(request, _(message))
    redirect_url = self.get_unauthorised_redirect_url(request)
    return redirect_to_login(request.get_full_path(), login_url=redirect_url)