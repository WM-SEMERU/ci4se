def form_valid(self, form):
    instance = form.save(commit=False)
    if hasattr(self.request, 'user'):
        instance.user = self.request.user
    if settings.CONTACT_FORM_FILTER_MESSAGE:
        instance.message = bleach.clean(instance.message, tags=settings.
            CONTACT_FORM_ALLOWED_MESSAGE_TAGS, strip=settings.
            CONTACT_FORM_STRIP_MESSAGE)
    instance.ip = get_user_ip(self.request)
    instance.site = self.site
    instance.save()
    if settings.CONTACT_FORM_USE_SIGNALS:
        contact_form_valid.send(sender=self, event=self.valid_event, ip=
            instance.ip, site=self.site, sender_name=instance.sender_name,
            sender_email=instance.sender_email, email=instance.subject.
            department.email, subject=instance.subject.title, message=
            instance.message)
    return super(ContactFormView, self).form_valid(form)