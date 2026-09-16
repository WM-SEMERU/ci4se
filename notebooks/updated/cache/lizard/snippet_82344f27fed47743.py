def send_html_mail(subject, message, message_html, from_email,
    recipient_list, priority=None, fail_silently=False, auth_user=None,
    auth_password=None, headers={}):
    from django.utils.encoding import force_text
    from django.core.mail import EmailMultiAlternatives
    from mailer.models import make_message
    priority = get_priority(priority)
    subject = force_text(subject)
    message = force_text(message)
    msg = make_message(subject=subject, body=message, from_email=from_email,
        to=recipient_list, priority=priority)
    email = msg.email
    email = EmailMultiAlternatives(email.subject, email.body, email.
        from_email, email.to, headers=headers)
    email.attach_alternative(message_html, 'text/html')
    msg.email = email
    msg.save()
    return 1