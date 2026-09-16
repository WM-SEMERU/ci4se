def password(self, request, uuid=None):
    user = self.get_object()
    serializer = serializers.PasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    new_password = serializer.validated_data['password']
    user.set_password(new_password)
    user.save()
    return Response({'detail': _('Password has been successfully updated.')
        }, status=status.HTTP_200_OK)