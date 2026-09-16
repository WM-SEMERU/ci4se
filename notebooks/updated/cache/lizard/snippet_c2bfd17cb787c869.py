def page_not_found(request, template_name='errors/404.html'):
    context = {'STATIC_URL': settings.STATIC_URL, 'request_path': request.path}
    t = get_template(template_name)
    return HttpResponseNotFound(t.render(context, request))