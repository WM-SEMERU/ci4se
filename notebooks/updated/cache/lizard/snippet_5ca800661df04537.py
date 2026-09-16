def signup(request, **kwargs):
    if not ALLAUTH:
        return http.HttpResponse(_('allauth not installed...'))
    if request.method == 'POST' and 'login' in request.POST:
        form_class = LoginForm
        form = form_class(request.POST)
        redirect_field_name = 'next'
        success_url = get_default_redirect(request, redirect_field_name)
        if form.is_valid():
            return form.login(request, redirect_url=success_url)
    response = allauth_signup(request, **kwargs)
    return response