def change_email(self, old_email, new_email):
    log.info("[+] Changing account email to '{}'".format(new_email))
    return self._send_xmpp_element(account.ChangeEmailRequest(self.password,
        old_email, new_email))