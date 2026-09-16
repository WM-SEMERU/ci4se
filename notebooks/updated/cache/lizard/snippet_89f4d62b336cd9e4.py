def dispatch(self, request, *args, **kwargs):
    regSession = self.request.session.get(REG_VALIDATION_STR, {})
    if not regSession:
        return HttpResponseRedirect(reverse('registration'))
    try:
        reg = TemporaryRegistration.objects.get(id=self.request.session[
            REG_VALIDATION_STR].get('temporaryRegistrationId'))
    except ObjectDoesNotExist:
        messages.error(request, _(
            'Invalid registration identifier passed to summary view.'))
        return HttpResponseRedirect(reverse('registration'))
    expiry = parse_datetime(self.request.session[REG_VALIDATION_STR].get(
        'temporaryRegistrationExpiry', ''))
    if not expiry or expiry < timezone.now():
        messages.info(request, _(
            'Your registration session has expired. Please try again.'))
        return HttpResponseRedirect(reverse('registration'))
    kwargs.update({'reg': reg})
    return super(RegistrationSummaryView, self).dispatch(request, *args, **
        kwargs)