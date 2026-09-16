def disqus_sso_script(context):
    settings = context['settings']
    public_key = getattr(settings, 'COMMENTS_DISQUS_API_PUBLIC_KEY', '')
    secret_key = getattr(settings, 'COMMENTS_DISQUS_API_SECRET_KEY', '')
    user = context['request'].user
    if public_key and secret_key and user.is_authenticated():
        context['public_key'] = public_key
        context['sso_data'] = _get_disqus_sso(user, public_key, secret_key)
    return context