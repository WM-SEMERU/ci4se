def verify_refresh_request(request):
    jwtauth_settings = request.app.settings.jwtauth.__dict__.copy()
    identity_policy = JWTIdentityPolicy(**jwtauth_settings)
    return identity_policy.verify_refresh(request)