def perform_login(request, user, email_verification, redirect_url=None,
    signal_kwargs=None, signup=False):
    adapter = get_adapter(request)
    if not user.is_active:
        return adapter.respond_user_inactive(request, user)
    from .models import EmailAddress
    has_verified_email = EmailAddress.objects.filter(user=user, verified=True
        ).exists()
    if email_verification == EmailVerificationMethod.NONE:
        pass
    elif email_verification == EmailVerificationMethod.OPTIONAL:
        if not has_verified_email and signup:
            send_email_confirmation(request, user, signup=signup)
    elif email_verification == EmailVerificationMethod.MANDATORY:
        if not has_verified_email:
            send_email_confirmation(request, user, signup=signup)
            return adapter.respond_email_verification_sent(request, user)
    try:
        adapter.login(request, user)
        response = HttpResponseRedirect(get_login_redirect_url(request,
            redirect_url))
        if signal_kwargs is None:
            signal_kwargs = {}
        signals.user_logged_in.send(sender=user.__class__, request=request,
            response=response, user=user, **signal_kwargs)
        adapter.add_message(request, messages.SUCCESS,
            'account/messages/logged_in.txt', {'user': user})
    except ImmediateHttpResponse as e:
        response = e.response
    return response