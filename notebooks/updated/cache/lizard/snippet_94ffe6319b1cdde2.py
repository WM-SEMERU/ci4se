def login(self, request):
    try:
        user = authenticate(request)
        if not user:
            raise AuthenticationFailed('User not authenticated.')
        if not user.is_active:
            raise AuthenticationFailed('This user has been disabled.')
        login(request, user)
        return Response(UserSerializer(user).data)
    except AuthError as ex:
        newrelic.agent.record_exception()
        logger.exception('Error', exc_info=ex)
        raise AuthenticationFailed(str(ex))