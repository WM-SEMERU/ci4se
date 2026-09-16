def create_user(self, username, email, password, active=False, send_email=True
    ):
    user = super(AccountActivationManager, self).create_user(username,
        email, password)
    if isinstance(user.username, str):
        username = user.username.encode('utf-8')
    salt, activation_key = generate_sha1(username)
    user.is_active = active
    user.activation_key = activation_key
    user.save(using=self._db)
    if send_email:
        user.send_activation_email()
    return user