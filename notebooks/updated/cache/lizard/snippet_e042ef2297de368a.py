def forbidden(request):
    template = pkg_resources.resource_string('pyramid_persona',
        'templates/forbidden.html').decode()
    html = template % {'js': request.persona_js, 'button': request.
        persona_button}
    return Response(html, status='403 Forbidden')