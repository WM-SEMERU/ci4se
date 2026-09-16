def sendmail_proxy(subject, email, template, **context):
    sendmail.delay(subject.value, email, template, **context)