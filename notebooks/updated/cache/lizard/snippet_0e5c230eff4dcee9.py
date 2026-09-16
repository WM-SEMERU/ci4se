def direct_to_user_template(request, username, template_name, extra_context
    =None):
    user = get_object_or_404(get_user_model(), username__iexact=username)
    if not extra_context:
        extra_context = dict()
    extra_context['viewed_user'] = user
    extra_context['profile'] = user.get_profile()
    return ExtraContextTemplateView.as_view(template_name=template_name,
        extra_context=extra_context)(request)