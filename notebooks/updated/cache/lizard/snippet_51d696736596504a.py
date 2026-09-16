def email_message(self, user, subject_template, body_template, sender=None,
    message_class=EmailMessage, **kwargs):
    if sender:
        try:
            display_name = sender.get_full_name()
        except (AttributeError, TypeError):
            display_name = sender.get_username()
        from_email = '%s <%s>' % (display_name, email.utils.parseaddr(
            settings.DEFAULT_FROM_EMAIL)[1])
        reply_to = '%s <%s>' % (display_name, sender.email)
    else:
        from_email = settings.DEFAULT_FROM_EMAIL
        reply_to = from_email
    headers = {'Reply-To': reply_to}
    kwargs.update({'sender': sender, 'user': user})
    subject_template = loader.get_template(subject_template)
    body_template = loader.get_template(body_template)
    subject = subject_template.render(kwargs).strip()
    body = body_template.render(kwargs)
    return message_class(subject, body, from_email, [user.email], headers=
        headers)