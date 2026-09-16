def authenticated(self):
    try:
        self.user = models.User.objects.get(username=self.request.session.
            get('username'), session_key=self.request.session.session_key)
    except models.User.DoesNotExist:
        logger.warning(
            'User %s seems authenticated but is not found in the database.' %
            (self.request.session.get('username'),))
        self.logout()
        if self.ajax:
            data = {'status': 'error', 'detail': 'login required', 'url':
                utils.reverse_params('cas_server:login', params=self.
                request.GET)}
            return json_response(self.request, data)
        else:
            return utils.redirect_params('cas_server:login', params=self.
                request.GET)
    if self.service:
        return self.service_login()
    elif self.ajax:
        data = {'status': 'success', 'detail': 'logged'}
        return json_response(self.request, data)
    else:
        return render(self.request, settings.CAS_LOGGED_TEMPLATE, utils.
            context({'session': self.request.session}))