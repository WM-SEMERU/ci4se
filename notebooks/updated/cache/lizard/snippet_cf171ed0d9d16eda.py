def get_proxy(self, input_):
    if input_._http_request is not None:
        authentication = DjangoAuthentication()
        authentication.set_django_user(input_._http_request.user, input_.
            _use_user_id)
    elif input_._xblock_user is not None:
        authentication = XBlockAuthentication()
        authentication.set_xblock_user(input_._xblock_user)
    else:
        authentication = None
    if authentication is not None:
        effective_agent_id = authentication.get_agent_id()
    else:
        effective_agent_id = input_._effective_agent_id
    if input_._locale is not None:
        locale = input_._locale
    else:
        locale = None
    return rules.Proxy(authentication=authentication, effective_agent_id=
        effective_agent_id, locale=locale)