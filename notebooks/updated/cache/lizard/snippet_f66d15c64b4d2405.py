def destroy(self, request, pk=None):
    user = self.get_object()
    user.is_active = False
    user.save()
    return Response(status=status.HTTP_204_NO_CONTENT)