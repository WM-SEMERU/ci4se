def activate_retry(request, activation_key, template_name=
    'userena/activate_retry_success.html', extra_context=None):
    if not userena_settings.USERENA_ACTIVATION_RETRY:
        return redirect(reverse('userena_activate', args=(activation_key,)))
    try:
        if UserenaSignup.objects.check_expired_activation(activation_key):
            new_key = UserenaSignup.objects.reissue_activation(activation_key)
            if new_key:
                if not extra_context:
                    extra_context = dict()
                return ExtraContextTemplateView.as_view(template_name=
                    template_name, extra_context=extra_context)(request)
            else:
                return redirect(reverse('userena_activate', args=(
                    activation_key,)))
        else:
            return redirect(reverse('userena_activate', args=(activation_key,))
                )
    except UserenaSignup.DoesNotExist:
        return redirect(reverse('userena_activate', args=(activation_key,)))