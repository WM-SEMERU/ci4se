def get_response_page(request, return_type, template_location,
    response_page_type):
    try:
        page = models.ResponsePage.objects.get(is_active=True, type=
            response_page_type)
        template = loader.get_template(template_location)
        content_type = None
        body = template.render(RequestContext(request, {'request_path':
            request.path, 'page': page}))
        return return_type(body, content_type=content_type)
    except models.ResponsePage.DoesNotExist:
        return None