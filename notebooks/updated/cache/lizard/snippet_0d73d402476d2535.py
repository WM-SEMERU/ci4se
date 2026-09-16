def send_password_changed_email(self, user):
    if not self.user_manager.USER_ENABLE_EMAIL:
        return
    if not self.user_manager.USER_SEND_PASSWORD_CHANGED_EMAIL:
        return
    user_or_user_email_object = (self.user_manager.db_manager.
        get_primary_user_email_object(user))
    email = user_or_user_email_object.email
    self._render_and_send_email(email, user, self.user_manager.
        USER_PASSWORD_CHANGED_EMAIL_TEMPLATE)