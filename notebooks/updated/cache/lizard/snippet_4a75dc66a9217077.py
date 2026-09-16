def iter_user_identities(user):
    from indico_vc_vidyo.plugin import VidyoPlugin
    providers = authenticators_re.split(VidyoPlugin.settings.get(
        'authenticators'))
    done = set()
    for provider in providers:
        for _, identifier in user.iter_identifiers(check_providers=True,
            providers={provider}):
            if identifier in done:
                continue
            done.add(identifier)
            yield identifier