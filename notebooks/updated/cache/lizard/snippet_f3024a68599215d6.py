def post(self, request, *args, **kwargs):
    return_url = request.POST.get('returnTo', '/')
    terms_ids = request.POST.getlist('terms')
    if not terms_ids:
        return HttpResponseRedirect(return_url)
    if DJANGO_VERSION <= (2, 0, 0):
        user_authenticated = request.user.is_authenticated()
    else:
        user_authenticated = request.user.is_authenticated
    if user_authenticated:
        user = request.user
    elif 'partial_pipeline' in request.session:
        user_pk = request.session['partial_pipeline']['kwargs']['user']['pk']
        user = User.objects.get(id=user_pk)
    else:
        return HttpResponseRedirect('/')
    store_ip_address = getattr(settings, 'TERMS_STORE_IP_ADDRESS', True)
    if store_ip_address:
        ip_address = request.META.get(getattr(settings,
            'TERMS_IP_HEADER_NAME', DEFAULT_TERMS_IP_HEADER_NAME))
    else:
        ip_address = ''
    for terms_id in terms_ids:
        try:
            new_user_terms = UserTermsAndConditions(user=user, terms=
                TermsAndConditions.objects.get(pk=int(terms_id)),
                ip_address=ip_address)
            new_user_terms.save()
        except IntegrityError:
            pass
    return HttpResponseRedirect(return_url)