def get_object(self, queryset=None):
    obj = User.objects.get(id=self.request.user.id)
    return obj