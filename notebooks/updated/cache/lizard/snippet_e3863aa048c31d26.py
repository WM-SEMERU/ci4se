def superuser_required(view_func):

    @wraps(view_func)
    def _checklogin(request, *args, **kwargs):
        if request.user.is_active and request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        assert hasattr(request, 'session'
            ), "The Django admin requires session middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."
        defaults = {'template_name': 'admin/login.html',
            'redirect_field_name': request.get_full_path(),
            'authentication_form': AdminAuthenticationForm, 'extra_context':
            {'title': _('Log in'), 'app_path': request.get_full_path()}}
        return LoginView(request, **defaults)
    return _checklogin