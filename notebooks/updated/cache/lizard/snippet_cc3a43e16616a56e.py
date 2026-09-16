def confirm_email(self, confirmation_key):
    if SHA1_RE.search(confirmation_key):
        try:
            userena = self.get(email_confirmation_key=confirmation_key,
                email_unconfirmed__isnull=False)
        except self.model.DoesNotExist:
            return False
        else:
            user = userena.user
            old_email = user.email
            user.email = userena.email_unconfirmed
            userena.email_unconfirmed, userena.email_confirmation_key = '', ''
            userena.save(using=self._db)
            user.save(using=self._db)
            userena_signals.confirmation_complete.send(sender=None, user=
                user, old_email=old_email)
            return user
    return False