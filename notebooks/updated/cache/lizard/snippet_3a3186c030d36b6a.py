def resend_welcome_message(self, user, base_url):
    user.require_email_confirmation()
    self.save(user)
    self.send_welcome_message(user, base_url)