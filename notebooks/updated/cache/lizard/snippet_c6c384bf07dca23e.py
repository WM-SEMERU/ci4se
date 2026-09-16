def send_email(to=None, message=None, template='base', context={}, subject=None
    ):
    from_email = settings.DEFAULT_FROM_EMAIL
    if to is None:
        if len(settings.ADMINS) > 0:
            to = settings.ADMINS[0][1]
        else:
            raise AttributeError('Not Admins defined')
    if isinstance(to, (tuple, str)) or isinstance(to, (list, str)):
        pass
    elif unicode:
        if not isinstance(to, unicode):
            raise TypeError(
                'email_to parameter has to be a List, Tuple or a String')
    else:
        raise TypeError(
            'email_to parameter has to be a List, Tuple or a String')
    email_to = to if isinstance(to, tuple) else (to,)
    context.update(get_default_context())
    if message is not None:
        context.update({'message': message})
    try:
        email_template = get_email_template(template)
    except EmailTemplateNotFound:
        email_template = get_email_template('email/base')
    email_subject = subject or 'System Notification'
    if email_template.get('txt'):
        template_txt = email_template.get('txt')
        msg = EmailMultiAlternatives(email_subject, template_txt.render(
            context), from_email, email_to)
        if email_template.get('html'):
            template_html = email_template.get('html')
            html_content = template_html.render(context)
            msg.attach_alternative(html_content, 'text/html')
        return msg.send()
    else:
        raise AttributeError('.txt template does not exist')
    raise Exception('Could Not Send Email')