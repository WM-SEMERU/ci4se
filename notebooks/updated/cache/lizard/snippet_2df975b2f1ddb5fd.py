def switch(request, tenant_id, redirect_field_name=auth.REDIRECT_FIELD_NAME):
    LOG.debug('Switching to tenant %s for user "%s".', tenant_id, request.
        user.username)
    endpoint, __ = utils.fix_auth_url_version_prefix(request.user.endpoint)
    session = utils.get_session()
    unscoped_token = request.user.unscoped_token
    auth = utils.get_token_auth_plugin(auth_url=endpoint, token=
        unscoped_token, project_id=tenant_id)
    try:
        auth_ref = auth.get_access(session)
        msg = 'Project switch successful for user "%(username)s".' % {
            'username': request.user.username}
        LOG.info(msg)
    except keystone_exceptions.ClientException:
        msg = _('Project switch failed for user "%(username)s".') % {'username'
            : request.user.username}
        messages.error(request, msg)
        auth_ref = None
        LOG.exception('An error occurred while switching sessions.')
    redirect_to = request.GET.get(redirect_field_name, '')
    if not is_safe_url(url=redirect_to, host=request.get_host()):
        redirect_to = settings.LOGIN_REDIRECT_URL
    if auth_ref:
        user = auth_user.create_user_from_token(request, auth_user.Token(
            auth_ref, unscoped_token=unscoped_token), endpoint)
        auth_user.set_session_from_user(request, user)
        message = _('Switch to project "%(project_name)s" successful.') % {
            'project_name': request.user.project_name}
        messages.success(request, message)
    response = shortcuts.redirect(redirect_to)
    utils.set_response_cookie(response, 'recent_project', request.user.
        project_id)
    return response