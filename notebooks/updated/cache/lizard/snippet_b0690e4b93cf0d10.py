def echo_attributes(request, config_loader_path=None, template=
    'djangosaml2/echo_attributes.html'):
    state = StateCache(request.session)
    conf = get_config(config_loader_path, request)
    client = Saml2Client(conf, state_cache=state, identity_cache=
        IdentityCache(request.session))
    subject_id = _get_subject_id(request.session)
    try:
        identity = client.users.get_identity(subject_id,
            check_not_on_or_after=False)
    except AttributeError:
        return HttpResponse(
            'No active SAML identity found. Are you sure you have logged in via SAML?'
            )
    return render(request, template, {'attributes': identity[0]})