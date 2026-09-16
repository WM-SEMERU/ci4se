def require_auth(view_func):
    from horizon.exceptions import NotAuthenticated

    @functools.wraps(view_func, assigned=available_attrs(view_func))
    def dec(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        raise NotAuthenticated(_('Please log in to continue.'))
    return dec