def override_template(template, content_type=None):
    request.pecan['override_template'] = template
    if content_type:
        request.pecan['override_content_type'] = content_type