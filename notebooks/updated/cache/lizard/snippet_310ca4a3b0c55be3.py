def get_first_recipient_with_address(self):
    recipients_with_address = [recipient for recipient in self._recipients if
        recipient.address]
    if recipients_with_address:
        return recipients_with_address[0]
    else:
        return None