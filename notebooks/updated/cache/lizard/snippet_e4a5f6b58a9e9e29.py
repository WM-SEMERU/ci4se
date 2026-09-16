def get_token_credentials(cls, username, request):
    try:
        user = cls.get_item(username=username)
    except Exception as ex:
        log.error(str(ex))
        forget(request)
    else:
        if user:
            return user.api_key.token