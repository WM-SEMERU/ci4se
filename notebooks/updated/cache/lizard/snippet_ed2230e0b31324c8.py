def is_all_field_none(self):
    if self._iban is not None:
        return False
    if self._display_name is not None:
        return False
    if self._avatar is not None:
        return False
    if self._label_user is not None:
        return False
    if self._country is not None:
        return False
    if self._bunq_me is not None:
        return False
    if self._is_light is not None:
        return False
    if self._swift_bic is not None:
        return False
    if self._swift_account_number is not None:
        return False
    if self._transferwise_account_number is not None:
        return False
    if self._transferwise_bank_code is not None:
        return False
    return True