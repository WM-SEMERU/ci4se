def new_message_email(sender, instance, signal, subject_prefix=_(
    'New Message: %(subject)s'), template_name=
    'django_messages/new_message.html', default_protocol=None, *args, **kwargs
    ):
    if default_protocol is None:
        default_protocol = getattr(settings, 'DEFAULT_HTTP_PROTOCOL', 'http')
    if 'created' in kwargs and kwargs['created']:
        try:
            current_domain = Site.objects.get_current().domain
            subject = subject_prefix % {'subject': instance.subject}
            message = render_to_string(template_name, {'site_url': 
                '%s://%s' % (default_protocol, current_domain), 'message':
                instance})
            if instance.recipient.email != '':
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [
                    instance.recipient.email])
        except Exception as e:
            pass