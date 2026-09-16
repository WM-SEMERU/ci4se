def send(self, request, pk=None):
    schedule = self.get_object()
    queue_subscription_send.delay(str(schedule.id))
    return Response({}, status=status.HTTP_202_ACCEPTED)