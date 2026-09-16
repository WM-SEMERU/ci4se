def post(self, request, *args, **kwargs):
    schedule_disable.delay(kwargs['subscription_id'])
    return Response({'accepted': True}, status=201)