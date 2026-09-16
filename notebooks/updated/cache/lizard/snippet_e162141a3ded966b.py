def custom_server_error(request, template_name='500.html',
    admin_template_name='500A.html'):
    trace = None
    if request.user.is_authenticated() and (request.user.is_staff or
        request.user.is_superuser):
        try:
            import traceback, sys
            trace = traceback.format_exception(*sys.exc_info())
            if not request.user.is_superuser and trace:
                trace = trace[-1:]
            trace = '\n'.join(trace)
        except:
            pass
    if request.path.startswith('/%s' % admin.site.name):
        template_name = admin_template_name
    t = loader.get_template(template_name)
    return http.HttpResponseServerError(t.render(Context({'trace': trace})))