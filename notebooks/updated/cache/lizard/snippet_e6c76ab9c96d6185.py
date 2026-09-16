def parse(self, request):
    assert isinstance(request, HttpRequest), 'Invalid request type: %s' % type(
        request)
    try:
        subject = request.POST.get('subject', '')
        text = '%s\n\n%s' % (request.POST.get('stripped-text', ''), request
            .POST.get('stripped-signature', ''))
        html = request.POST.get('stripped-html')
        from_email = request.POST.get('sender')
        to_email = request.POST.get('recipient').split(',')
        cc = request.POST.get('cc', '').split(',')
        bcc = request.POST.get('bcc', '').split(',')
    except MultiValueDictKeyError as ex:
        raise RequestParseError(
            'Inbound request is missing required value: %s.' % ex)
    except AttributeError as ex:
        raise RequestParseError(
            'Inbound request is missing required value: %s.' % ex)
    email = EmailMultiAlternatives(subject=subject, body=text, from_email=
        from_email, to=to_email, cc=cc, bcc=bcc)
    if html is not None and len(html) > 0:
        email.attach_alternative(html, 'text/html')
    for n, f in list(request.FILES.items()):
        if f.size > self.max_file_size:
            logger.debug('File attachment %s is too large to process (%sB)',
                f.name, f.size)
            raise AttachmentTooLargeError(email=email, filename=f.name,
                size=f.size)
        else:
            email.attach(n, f.read(), f.content_type)
    return email