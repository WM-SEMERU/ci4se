def _setup_apikey_policy(config, params):
    from nefertari.authentication.views import TokenAuthRegisterView, TokenAuthClaimView, TokenAuthResetView
    log.info('Configuring ApiKey Authn policy')
    auth_model = config.registry.auth_model
    params['check'] = auth_model.get_groups_by_token
    params['credentials_callback'] = auth_model.get_token_credentials
    params['user_model'] = auth_model
    config.add_request_method(auth_model.get_authuser_by_name, 'user',
        reify=True)
    policy = ApiKeyAuthenticationPolicy(**params)
    RegisterViewBase = TokenAuthRegisterView
    if config.registry.database_acls:


        class RegisterViewBase(ACLAssignRegisterMixin, TokenAuthRegisterView):
            pass


    class RamsesTokenAuthRegisterView(RegisterViewBase):
        Model = auth_model


    class RamsesTokenAuthClaimView(TokenAuthClaimView):
        Model = auth_model


    class RamsesTokenAuthResetView(TokenAuthResetView):
        Model = auth_model
    common_kw = {'prefix': 'auth', 'factory': 'nefertari.acl.AuthenticationACL'
        }
    root = config.get_root_resource()
    root.add('register', view=RamsesTokenAuthRegisterView, **common_kw)
    root.add('token', view=RamsesTokenAuthClaimView, **common_kw)
    root.add('reset_token', view=RamsesTokenAuthResetView, **common_kw)
    return policy