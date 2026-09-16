def signup(request, template='accounts/account_signup.html', extra_context=None
    ):
    profile_form = get_profile_form()
    form = profile_form(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        new_user = form.save()
        if not new_user.is_active:
            if settings.ACCOUNTS_APPROVAL_REQUIRED:
                send_approve_mail(request, new_user)
                info(request, _(
                    "Thanks for signing up! You'll receive an email when your account is activated."
                    ))
            else:
                send_verification_mail(request, new_user, 'signup_verify')
                info(request, _(
                    'A verification email has been sent with a link for activating your account.'
                    ))
            return redirect(next_url(request) or '/')
        else:
            info(request, _('Successfully signed up'))
            auth_login(request, new_user)
            return login_redirect(request)
    context = {'form': form, 'title': _('Sign up')}
    context.update(extra_context or {})
    return TemplateResponse(request, template, context)