def dispatch(self, request, *args, **kwargs):

    def wrapper(request, *args, **kwargs):
        if not self.has_permission(request, *args, **kwargs):
            path = urlquote(request.get_full_path())
            login_url = kwargs.pop('login_url', settings.LOGIN_URL)
            redirect_field_name = kwargs.pop('redirect_field_name',
                REDIRECT_FIELD_NAME)
            return HttpResponseRedirect('%s?%s=%s' % (login_url,
                redirect_field_name, path))
        else:
            response = self.pre_process(request, *args, **kwargs)
            if not response:
                return super(SmartView, self).dispatch(request, *args, **kwargs
                    )
            else:
                return response
    return wrapper(request, *args, **kwargs)