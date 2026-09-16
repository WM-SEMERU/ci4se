def client_has_user_consent(self):
    value = False
    try:
        uc = UserConsent.objects.get(user=self.request.user, client=self.client
            )
        if set(self.params['scope']).issubset(uc.scope) and not uc.has_expired(
            ):
            value = True
    except UserConsent.DoesNotExist:
        pass
    return value