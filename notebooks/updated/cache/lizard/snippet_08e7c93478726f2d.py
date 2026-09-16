def send_registered_email(self, user, user_email, request_email_confirmation):
    if not self.user_manager.USER_ENABLE_EMAIL:
        return
    if not self.user_manager.USER_SEND_REGISTERED_EMAIL:
        return
    email = user_email.email if user_email else user.email
    if request_email_confirmation:
        token = self.user_manager.generate_token(user_email.id if
            user_email else user.id)
        confirm_email_link = url_for('user.confirm_email', token=token,
            _external=True)
    else:
        confirm_email_link = None
    self._render_and_send_email(email, user, self.user_manager.
        USER_REGISTERED_EMAIL_TEMPLATE, confirm_email_link=confirm_email_link)