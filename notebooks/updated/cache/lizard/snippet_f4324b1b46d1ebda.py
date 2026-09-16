def is_all_field_none(self):
    if self._monetary_account_id is not None:
        return False
    if self._alias is not None:
        return False
    if self._counterparty_alias is not None:
        return False
    if self._amount_guaranteed is not None:
        return False
    if self._amount_requested is not None:
        return False
    if self._issuer is not None:
        return False
    if self._issuer_authentication_url is not None:
        return False
    if self._status is not None:
        return False
    if self._error_message is not None:
        return False
    if self._transaction_identifier is not None:
        return False
    return True