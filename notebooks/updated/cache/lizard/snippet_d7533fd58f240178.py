def mark_thread_as_read(self, request, pk=None):
    thread = Thread.objects.get(id=pk)
    self.check_object_permissions(request, thread)
    try:
        participation = Participation.objects.get(thread=thread,
            participant=request.rest_messaging_participant)
        participation.date_last_check = now()
        participation.save()
        serializer = self.get_serializer(thread)
        return Response(serializer.data)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)