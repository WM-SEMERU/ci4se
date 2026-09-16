def handler404(request, template_name='404.html'):
    t = loader.get_template(template_name)
    return http.HttpResponseNotFound(t.render(Context({'MEDIA_URL':
        settings.MEDIA_URL, 'STATIC_URL': settings.STATIC_URL})))