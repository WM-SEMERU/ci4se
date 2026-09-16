def format_request_email_body(increq, **ctx):
    template = current_app.config['COMMUNITIES_REQUEST_EMAIL_BODY_TEMPLATE'],
    return format_request_email_templ(increq, template, **ctx)