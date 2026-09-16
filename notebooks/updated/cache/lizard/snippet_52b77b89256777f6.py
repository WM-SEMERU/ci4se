def sudo_required(func):

    @wraps(func)
    def inner(request, *args, **kwargs):
        if not request.is_sudo():
            return redirect_to_sudo(request.get_full_path())
        return func(request, *args, **kwargs)
    return inner