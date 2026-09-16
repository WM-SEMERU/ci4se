def add_user_to_template(self, template_id, account_id=None, email_address=None
    ):
    return self._add_remove_user_template(self.TEMPLATE_ADD_USER_URL,
        template_id, account_id, email_address)