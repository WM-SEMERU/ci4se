def register_by_email(self, email, sender=None, request=None, **kwargs):
    try:
        user = self.user_model.objects.get(email=email)
    except self.user_model.DoesNotExist:
        user = self.user_model.objects.create(username=self.get_username(),
            email=email, password=self.user_model.objects.
            make_random_password())
        user.is_active = False
        user.save()
    self.send_activation(user, sender, **kwargs)
    return user