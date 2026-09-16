def register_email(request):
    user = request.user
    serializer = RegisterEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']
    template_config = (registration_settings.
        REGISTER_EMAIL_VERIFICATION_EMAIL_TEMPLATES)
    if registration_settings.REGISTER_EMAIL_VERIFICATION_ENABLED:
        signer = RegisterEmailSigner({'user_id': user.pk, 'email': email},
            request=request)
        send_verification_notification(user, signer, template_config, email
            =email)
    else:
        email_field = get_user_setting('EMAIL_FIELD')
        setattr(user, email_field, email)
        user.save()
    return get_ok_response('Register email link email sent')