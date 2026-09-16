def server_error(request, template_name='errors/500.html'):
    context = {'STATIC_URL': settings.STATIC_URL}
    t = get_template(template_name)
    return HttpResponseServerError(t.render(context, request))