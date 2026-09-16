async def get_auth(request):
    auth_val = request.get(AUTH_KEY)
    if auth_val:
        return auth_val
    auth_policy = request.get(POLICY_KEY)
    if auth_policy is None:
        raise RuntimeError('auth_middleware not installed')
    request[AUTH_KEY] = await auth_policy.get(request)
    return request[AUTH_KEY]