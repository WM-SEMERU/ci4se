def send(self):
    if self.status is OUTWARD_STATUS.get('sent'):
        return False
    recipients = self.get_recipients()
    emails = []
    if OUTWARD_HTML:
        html_content = self.message
        EmailClass = EmailMultiAlternatives
    else:
        EmailClass = EmailMessage
    message = strip_tags(self.message)
    for recipient in recipients:
        msg = EmailClass(self.subject, message, settings.DEFAULT_FROM_EMAIL,
            [recipient])
        if OUTWARD_HTML:
            msg.attach_alternative(html_content, 'text/html')
        emails.append(msg)
    try:
        counter = 0
        for email in emails:
            if counter == OUTWARD_STEP:
                counter = 0
                time.sleep(OUTWARD_DELAY)
            email.send()
            counter += 1
    except socket.error as e:
        from logging import error
        error('nodeshot.core.mailing.models.outward.send(): %s' % e)
        self.status = OUTWARD_STATUS.get('error')
    self.status = OUTWARD_STATUS.get('sent')
    self.save()