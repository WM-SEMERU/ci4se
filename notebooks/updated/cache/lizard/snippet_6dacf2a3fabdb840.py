def userinfo(access_token, scope_request=None, claims_request=None):
    handlers = HANDLERS['userinfo']
    claims_request_section = claims_request.get('userinfo', {}
        ) if claims_request else {}
    if not scope_request and not claims_request_section:
        scope_request = provider.scope.to_names(access_token.scope)
    else:
        scope_request = scope_request
    scopes, claims = collect(handlers, access_token, scope_request=
        scope_request, claims_request=claims_request_section)
    return IDToken(access_token, scopes, claims)