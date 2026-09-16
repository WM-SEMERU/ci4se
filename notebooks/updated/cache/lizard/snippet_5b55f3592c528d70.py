def process_view(self, request, view_func, view_args, view_kwargs):
    try:
        if ignore_path(request.path):
            TrackedRequest.instance().tag('ignore_transaction', True)
        view_name = request.resolver_match._func_path
        span = TrackedRequest.instance().current_span()
        if span is not None:
            span.operation = 'Controller/' + view_name
            Context.add('path', request.path)
            Context.add('user_ip', RemoteIp.lookup_from_headers(request.META))
            if getattr(request, 'user', None) is not None:
                Context.add('username', request.user.get_username())
    except Exception:
        pass