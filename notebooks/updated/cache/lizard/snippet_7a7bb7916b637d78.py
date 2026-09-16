def send_email_from_template(to_email, from_email, subject,
    markdown_template=None, text_template=None, html_template=None,
    fail_silently=False, context=None, **kwargs):
    return send_emails_from_template(to_emails=[to_email], from_email=
        from_email, subject=subject, markdown_template=markdown_template,
        text_template=text_template, html_template=html_template,
        fail_silently=fail_silently, context=context, **kwargs)