def create_token(request):
    token = GATEWAY.get_token(request)
    return Response({'token': token}, status=status.HTTP_200_OK)