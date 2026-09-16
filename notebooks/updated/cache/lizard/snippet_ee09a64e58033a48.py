def login_required(f, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):

    @wraps(f)
    def wrapper(request, *args, **kwargs):
        if is_authenticated(request.user):
            return f(request, *args, **kwargs)
        shopify_params = {k: request.GET[k] for k in ['shop', 'timestamp',
            'signature', 'hmac'] if k in request.GET}
        resolved_login_url = force_str(resolve_url(login_url or settings.
            LOGIN_URL))
        updated_login_url = add_query_parameters_to_url(resolved_login_url,
            shopify_params)
        django_login_required_decorator = django_login_required(
            redirect_field_name=redirect_field_name, login_url=
            updated_login_url)
        return django_login_required_decorator(f)(request, *args, **kwargs)
    return wrapper